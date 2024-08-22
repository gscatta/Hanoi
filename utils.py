from dataclasses import dataclass
from os import system
from typing import Callable
from hanoi import Hanoi


@dataclass(frozen=True)
class Style:
    HEADER = "\033[95m"
    COPY = "\033[36m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    HIGHLIGHT = "\033[44m"

    @staticmethod
    def set(message: str, style: str, inline = False):
        left_padding = '       '
        stylized_message = style + message + Style.ENDC
        if inline:
            return stylized_message
        return left_padding + stylized_message


@dataclass(frozen=True)
class CommandList:
    quitting_commands = ["quit", "q"]
    moving_commands = ["12", "13", "21", "23", "31", "33"]
    help_commands = ["help", "h", "--help"]
    commands_whitelist = quitting_commands + moving_commands + help_commands
    error_message = (
        "command not valid; use [help] or [h] for the list of available commands"
    )


class Command(CommandList):
    def __init__(self):
        self.command = ""

    def get(self):
        return self.command

    def input(self):
        self.command = input(f"{Style.set("  insert command:  ", Style.HIGHLIGHT)} ")

    def is_not_valid(self) -> bool:
        return self.command and self.command not in self.commands_whitelist


class UI:
    __default_title = "------- TOWER OF HANOI -------"
    __copyright = "©Giorgio Scattareggia"
    __center_space = "                    "

    def __init__(self, hanoi: Hanoi, title: str = __default_title) -> None:
        self.hanoi = hanoi
        self.title = title + self.__center_space + Style.set(self.__copyright, Style.COPY, True)
        self.command = Command()

    def clear(self, show_hanoi: bool = True):
        system("clear")
        print('\n\n\n')
        print(Style.set(self.title, Style.BOLD + Style.HEADER))
        if show_hanoi:
            print(f"\n{self.hanoi}\n")

    def start(self, action: Callable[[Command, Hanoi], None]):
        while self.command.get() not in self.command.quitting_commands:
            action(self.command, self.hanoi)
            self.clear()
            if self.command.is_not_valid():
                print(Style.set(f"{self.command.error_message}\n", Style.WARNING))
            self.command.input()
        system('clear')
