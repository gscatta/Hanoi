from dataclasses import dataclass
from os import system
from typing import Callable
from hanoi import Hanoi
from help import Help


@dataclass(frozen=True)
class Layout:
    LINE_WIDTH = 85
    NUMBER_OF_LINES = 24
    X_PADDING = 7
    Y_PADDING = 3

    @staticmethod
    def px(span: str):
        return Layout.X_PADDING * " " + span


@dataclass(frozen=True)
class Style:
    HEADER = "\033[95m"
    COPY = "\033[36m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    HIGHLIGHT = "\033[44m"
    ENDC = "\033[0m"

    @staticmethod
    def set(message: str, style: str, inline=False):
        stylized_message = style + message + Style.ENDC
        if inline:
            return stylized_message
        return Layout.px(stylized_message)


@dataclass(frozen=True)
class CommandList:
    quitting_commands = ["quit", "q"]
    moving_commands = ["12", "13", "21", "23", "31", "32"]
    help_commands = ["help", "h", "--help"]
    whitelist = quitting_commands + moving_commands + help_commands
    error_message = (
        "COMMAND NOT VALID! use [help] or [h] for the list of available commands"
    )


class Command(CommandList):
    def __init__(self):
        self.command = ""

    def get(self):
        return self.command.lower()

    def input(self):
        self.command = input(f"{Style.set('  insert command:  ', Style.HIGHLIGHT)} ")

    def is_not_valid(self) -> bool:
        return self.command != "" and self.command not in self.whitelist


class UI:
    __title = "------- TOWER OF HANOI -------"
    __copyright = "©Giorgio Scattareggia"

    def __init__(self, hanoi: Hanoi, title: str = __title) -> None:
        stylized_title = Style.set(title, Style.BOLD + Style.HEADER)
        stylized_copyright = Style.set(self.__copyright, Style.COPY, inline=True)
        center_space = (
            Layout.LINE_WIDTH
            - 2 * Layout.X_PADDING
            - len(title)
            - len(self.__copyright)
        )
        self.hanoi = hanoi
        self.header = stylized_title + center_space * " " + stylized_copyright
        self.command = Command()

    def render(self, show_hanoi: bool = True):
        system("clear")
        print(Layout.Y_PADDING * "\n")
        print(self.header)
        if show_hanoi:
            print(f"\n{self.hanoi}\n")

    def run(
        self, action: Callable[[str, Hanoi], tuple[int, IndexError | ValueError | None]]
    ):
        while self.command.get() not in self.command.quitting_commands:
            result, error = action(self.command.get(), self.hanoi)
            self.render()
            if self.command.get() in self.command.help_commands:
                print(Help.get_help())
            elif self.command.is_not_valid():
                print(Style.set(f"{self.command.error_message}\n", Style.WARNING))
            elif result == 1:
                print(Style.set(f"ERROR: {error}!\n", Style.FAIL))
            self.command.input()
        system("clear")
