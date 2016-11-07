import dd.generate_monitors

from click.testing import CliRunner


def test__cli_command_success(mocker):
    mocker.patch.object(dd.generate_monitors, 'initialize')
    mocker.patch.object(dd.generate_monitors.api, 'Monitor')

    dd.generate_monitors.api.Monitor.get_all.return_value = []
    dd.generate_monitors.api.Monitor.create.return_value = {}

    runner = CliRunner()
    result = runner.invoke(dd.generate_monitors.cli, ['--api-key', 'API_KEY', '--app-key', 'APP_KEY'])

    dd.generate_monitors.initialize.assert_called_once_with('API_KEY', 'APP_KEY')
    dd.generate_monitors.api.Monitor.create.assert_called()

    assert result.exit_code == 0
