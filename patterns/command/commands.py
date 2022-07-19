from patterns.command.exit_command import ExitCommand
from patterns.command.history_command import HistoryCommand
from patterns.command.redo_command import RedoCommand
from patterns.command.remove_command import RmCommand
from patterns.command.undo_command import UndoCommand
from patterns.command.uptime_command import UptimeCommand

history = HistoryCommand()
rm = RmCommand(history)
uptime = UptimeCommand(history)
undo = UndoCommand(history)
redo = RedoCommand(history)
exit = ExitCommand()


COMMANDS = {
    "rm": rm,
    "uptime": uptime,
    "undo": undo,
    "redo": redo,
    "history": history,
    "exit": exit,
}
