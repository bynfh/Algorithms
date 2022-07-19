from dataclasses import dataclass

from patterns.command.base_command import ICommand
from sys import stdout as console

from patterns.command.history_command import HistoryCommand


@dataclass
class RmCommand(ICommand):
    """IMPL rm command."""

    history: HistoryCommand

    def execute(self):
        self.history.add(self.name())
        console.write('You are executed "rm" command\n')

    def cancel(self):
        console.write('You are canceled "rm" command\n')

    @staticmethod
    def name():
        return "rm"
