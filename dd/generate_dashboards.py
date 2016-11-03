import click
import json
import os
import sys

from datadog import initialize, api

DASHBOARD_DIR = 'dd/dashboards'
DASHBOARD_REQUIRED_FIELDS = ['title', 'description', 'template_variables', 'graphs']


@click.command()
@click.option('--api-key', help='Datadog API key', required=True, envvar='DATADOG_API_KEY')
@click.option('--app-key', help='Datadog app key', required=True, envvar='DATADOG_APP_KEY')
def cli(api_key, app_key):
    # Initialize Datadog api access
    initialize(api_key, app_key)

    files = []
    for (dir_path, dir_names, file_names) in os.walk(DASHBOARD_DIR):
        files.extend(file_names)
        break

    for def_file in files:
        try:
            with open(os.path.join(DASHBOARD_DIR, def_file)) as f:
                dashboard_def = json.load(f)

            for attr in DASHBOARD_REQUIRED_FIELDS:
                if attr not in dashboard_def:
                    raise Exception('Missing graph attribute %s' % attr)

            title = dashboard_def['title']
            description = dashboard_def['description']
            template_variables = dashboard_def['template_variables']
            graphs = dashboard_def['graphs']

            read_only = True

            click.echo('Creating dashboard: %s' % title)

            api_response = api.Timeboard.create(title=title, description=description, graphs=graphs,
                                                template_variables=template_variables, read_only=read_only)
            if 'errors' in api_response and len(api_response['errors']) > 0:
                raise Exception("Failed to create dashboard with definition in %s" % def_file)
        except Exception as e:
            click.echo("Failed to create dashboard with definition in %s: %s" % (def_file, e))
            sys.exit(1)
