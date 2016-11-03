import click
import json
import os
import sys

from datadog import initialize, api

MONITOR_DIR = 'dd/monitors'
MONITOR_REQUIRED_FIELDS = ['tags', 'type', 'options', 'query', 'message']


@click.command()
@click.option('--api-key', help='Datadog API key', required=True, envvar='DATADOG_API_KEY')
@click.option('--app-key', help='Datadog app key', required=True, envvar='DATADOG_APP_KEY')
def cli(api_key, app_key):
    # Initialize Datadog api access
    initialize(api_key, app_key)

    # Get all the monitors currently created in datadog
    monitors = api.Monitor.get_all()
    monitor_name_id_map = {}
    for monitor in monitors:
        monitor_name_id_map[monitor['name']] = monitor['id']

    files = []
    for (dir_path, dir_names, file_names) in os.walk(MONITOR_DIR):
        files.extend(file_names)
        break

    for def_file in files:
        try:
            with open(os.path.join(MONITOR_DIR, def_file)) as f:
                monitor_def = json.load(f)

            for attr in MONITOR_REQUIRED_FIELDS:
                if attr not in monitor_def:
                    raise Exception('Missing monitor attribute %s' % attr)

            name = monitor_def['name']
            options = monitor_def.get('options', {})
            tags = monitor_def.get('tags', [])
            monitor_type = monitor_def['type']
            query = monitor_def['query']
            message = monitor_def['message']

            options['locked'] = True

            if name in monitor_name_id_map:
                click.echo('Updating monitor: %s' % name)
                api_response = api.Monitor.update(id=monitor_name_id_map[name], type=monitor_type, query=query,
                                                  name=name, message=message, tags=tags, options=options)
            else:
                click.echo('Creating monitor: %s' % name)
                api_response = api.Monitor.create(type=monitor_type, query=query, name=name, message=message,
                                                  tags=tags, options=options)

            if 'errors' in api_response and len(api_response['errors']) > 0:
                raise Exception(','.join(api_response['errors']))
        except Exception as e:
            click.echo("Failed to create/update monitor with definition in %s: %s" % (def_file, e))
            sys.exit(1)
