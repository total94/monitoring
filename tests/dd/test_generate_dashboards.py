import dd.generate_dashboards

from click.testing import CliRunner


def test__cli_command_success(mocker):
    mocker.patch.object(dd.generate_dashboards, 'initialize')
    mocker.patch.object(dd.generate_dashboards.api, 'Timeboard')

    dd.generate_dashboards.api.Timeboard.get_all.return_value = {'dashes': []}
    dd.generate_dashboards.api.Timeboard.create.return_value = {}

    runner = CliRunner()
    result = runner.invoke(dd.generate_dashboards.cli, ['--api-key', 'API_KEY', '--app-key', 'APP_KEY'])

    dd.generate_dashboards.initialize.assert_called_once_with('API_KEY', 'APP_KEY')
    dd.generate_dashboards.api.Timeboard.create.assert_called()

    assert result.exit_code == 0
