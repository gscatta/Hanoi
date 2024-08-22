from hanoi import Hanoi
from utils import Command, UI


def action(command: str, hanoi: Hanoi):
    if command in Command.moving_commands:
        try:
            from_tower, to_tower = (int(char) for char in command)
            hanoi.move_piece(from_tower, to_tower)
        except IndexError as error:
            return (1, error)
    return (0, None)


def main():
    hanoi = Hanoi(5)
    ui = UI(hanoi)
    ui.run(action)


if __name__ == "__main__":
    main()
