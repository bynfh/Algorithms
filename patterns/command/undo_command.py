from dataclasses import dataclass

from patterns.command.base_command import ICommand
from sys import stdout as console

from patterns.command.history_command import HistoryCommand


@dataclass
class UndoCommand(ICommand):
    """IMPL undo command."""

    history: HistoryCommand

    def execute(self):
        if self.history.is_empty_history:
            console.write("HISTORY is empty\n")
            return

        cmd = self.history.delete()
        console.write(f'Undo command "{cmd}"\n')

    def cancel(self):
        raise NotImplementedError()

    @staticmethod
    def name():
        return "undo"
