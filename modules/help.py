from dataclasses import dataclass


@dataclass(frozen=True)
class Help:
    HEADER = "----- AVAILABLE COMMANDS -----"
    MOVE = "[i][j]\t: move a piece from rod i to rod j (e.g.: 13 -> from 1 to 3)"
    HELP = "help or h: show the list of available commands"
    QUIT = "quit or q: quit the game"

    @staticmethod
    def get_help():
        from modules.ui import Layout, Style

        help_string = Style.set(Help.HEADER, Style.COPY + Style.BOLD) + "\n"
        help_string += Layout.px(Help.MOVE) + "\n"
        help_string += Layout.px(Help.HELP) + "\n"
        help_string += Layout.px(Help.QUIT) + "\n"
        return help_string
