from dataclasses import dataclass

from patterns.command.base_command import ICommand
from sys import stdout as console

from patterns.command.history_command import HistoryCommand


@dataclass
class UptimeCommand(ICommand):
    """IMPL uptime command."""

    history: HistoryCommand

    def execute(self):
        self.history.add(self.name())
        console.write('You are executed "uptime" command\n')

    def cancel(self):
        console.write('You are canceled "uptime" command\n')

    @staticmethod
    def name():
        return "uptime"
