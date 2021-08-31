"""It is example Command Pattern"""

from sys import stdout as console


# Обработка команды exit
class SessionClosed(Exception):
    def __init__(self, value):
        self.value = value


# Интерфейс команды
class Command:
    def execute(self):
        raise NotImplementedError()

    def cancel(self):
        raise NotImplementedError()

    @staticmethod
    def name():
        raise NotImplementedError()


# Команда rm
class RmCommand(Command):
    def execute(self):
        console.write("You are executed \"rm\" command\n")

    def cancel(self):
        console.write("You are canceled \"rm\" command\n")

    @staticmethod
    def name():
        return "rm"


# Команда uptime
class UptimeCommand(Command):
    def execute(self):
        console.write("You are executed \"uptime\" command\n")

    def cancel(self):
        console.write("You are canceled \"uptime\" command\n")

    @staticmethod
    def name():
        return "uptime"


# Команда undo
class UndoCommand(Command):
    def execute(self):
        try:
            cmd = HISTORY.pop()
            TRASH.append(cmd)
            console.write("Undo command \"{0}\"\n".format(cmd.name()))
            cmd.cancel()

        except IndexError:
            console.write("ERROR: HISTORY is empty\n")

    def cancel(self):
        raise NotImplementedError()

    @staticmethod
    def name():
        return "undo"


# Команда redo
class RedoCommand(Command):
    def execute(self):
        try:
            cmd = TRASH.pop()
            HISTORY.append(cmd)
            console.write("Redo command \"{0}\"\n".format(cmd.name()))
            cmd.execute()

        except IndexError:
            console.write("ERROR: TRASH is empty\n")

    def cancel(self):
        raise NotImplementedError()

    @staticmethod
    def name():
        return "redo"


# Команда history
class HistoryCommand(Command):
    def execute(self):
        i = 0
        for cmd in HISTORY:
            console.write("{0}: {1}\n".format(i, cmd.name()))
            i = i + 1

    def cancel(self):
        raise NotImplementedError()

    @staticmethod
    def name():
        return "history"


# Команда exit
class ExitCommand(Command):
    def execute(self):
        raise SessionClosed("Good bay!")

    def cancel(self):
        raise NotImplementedError()

    @staticmethod
    def name():
        return "exit"


# Словарь доступных команд
COMMANDS = {'rm': RmCommand(), 'uptime': UptimeCommand(), 'undo': UndoCommand(), 'redo': RedoCommand(),
            'history': HistoryCommand(), 'exit': ExitCommand()}

HISTORY = list()
TRASH = list()


# Шелл
def main():
    try:
        while True:
            console.flush()
            console.write("pysh >> ")

            cmd = input().lower()

            try:

                command = COMMANDS[cmd]
                command.execute()

                if not isinstance(command, UndoCommand) and not isinstance(command, RedoCommand) and not isinstance(
                        command, HistoryCommand):
                    TRASH = list()
                    HISTORY.append(command)

            except KeyError:
                console.write(f"ERROR: Command {cmd} not found\n")

    except SessionClosed as e:
        console.write(e.value)


if __name__ == "__main__":
    main()
