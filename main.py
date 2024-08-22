from hanoi import Hanoi
from utils import Command, UI


def action(command: Command, hanoi: Hanoi):
    if command.get() == "12":
        hanoi.move_piece(1, 2)


def main():
    hanoi = Hanoi(5)
    ui = UI(hanoi)
    ui.clear()
    ui.start(action)

    # s = Stack(1)

    # print(s)

    # s.append(2)

    # print(s)

    # print(s.pop())

    # print(s)

    # print(s.pop())

    # print(s)

    # q = Queue(1)
    # q.append(2)
    # q.append(3)

    # print(q)

    # print(q.pop())
    # print(q)


if __name__ == "__main__":
    main()
