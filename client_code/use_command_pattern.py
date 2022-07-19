from sys import stdout as console

from patterns.command.commands import COMMANDS
from patterns.command.exit_command import SessionClosed


def main():
    """In infinity loop read console.

    Get commands and execute them.
    """
    try:
        while True:
            console.flush()
            console.write("push >> ")
            cmd = input().lower()
            if cmd in COMMANDS:
                command = COMMANDS.get(cmd)
                command.execute()
            else:
                console.write(f"ERROR: Command {cmd} not found\n")
    except SessionClosed as e:
        console.write(e.value)


if __name__ == "__main__":
    main()
