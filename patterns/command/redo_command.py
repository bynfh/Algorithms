from dataclasses import dataclass

from patterns.command.base_command import ICommand
from sys import stdout as console

from patterns.command.history_command import HistoryCommand


@dataclass
class RedoCommand(ICommand):
    """IMPL redo command."""

    history: HistoryCommand

    def execute(self):
        if self.history.is_empty_trash:
            console.write("TRASH is empty\n")
            return

        cmd = self.history.restore()
        console.write(f'Redo command "{cmd}"\n')

    def cancel(self):
        raise NotImplementedError()

    @staticmethod
    def name():
        return "redo"
