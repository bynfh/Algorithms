from patterns.command.base_command import ICommand


class SessionClosed(Exception):
    def __init__(self, value):
        self.value = value


class ExitCommand(ICommand):
    def execute(self):
        raise SessionClosed("Good bay!")

    def cancel(self):
        raise NotImplementedError()

    @staticmethod
    def name():
        return "exit"
