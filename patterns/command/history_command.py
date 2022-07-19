from patterns.command.base_command import ICommand
from sys import stdout as console


class HistoryCommand(ICommand):
    """IMPL history command. Consider add, delete, restore methods for work
    with history.

    :history: store for command
    :trash: store for delete command
    """

    __history: list = []
    __trash: list = []

    def execute(self):
        if self.is_empty_history:
            console.write("History is empty.\n")

        for index, cmd in enumerate(self.__history, start=1):
            console.write(f"{index}: {cmd}\n")

    def add(self, cmd: str):
        """Add to history."""
        self.__history.append(cmd)

    def delete(self) -> str:
        """Delete from history."""
        cmd = self.__history.pop()
        self.__trash.append(cmd)
        return cmd

    def restore(self):
        """Recover from trash."""
        cmd = self.__trash.pop()
        self.__history.append(cmd)
        return cmd

    @property
    def is_empty_trash(self) -> bool:
        return self.__trash == []

    @property
    def is_empty_history(self) -> bool:
        return self.__history == []

    def cancel(self):
        raise NotImplementedError()

    @staticmethod
    def name():
        return "history"
