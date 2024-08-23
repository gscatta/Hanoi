from stack import Stack


class Hanoi:
    def __init__(self, k: int) -> None:
        if k < 1:
            raise ValueError("init Hanoi Towers with less than 1 piece")
        self.towers = (Stack[int](), Stack[int](), Stack[int]())
        for i in range(k, 0, -1):
            self.towers[0].append(i)

    def move_piece(self, from_tower: int, to_tower: int) -> None:
        if from_tower < 1 or from_tower > 3 or to_tower < 1 or to_tower > 3:
            raise IndexError("tower index out of range")
        if self.towers[from_tower - 1].is_empty():
            raise IndexError("illegal move. You can't pick a piece from an empty rod")
        if not self.towers[to_tower - 1].is_empty():
            piece_value = self.towers[from_tower - 1].get()
            landing_value = self.towers[to_tower - 1].get()
            if landing_value <= piece_value:
                raise ValueError(
                    "illegal move. Please follow the descending order of the pieces"
                )
        piece = self.towers[from_tower - 1].pop()
        self.towers[to_tower - 1].append(piece)

    def __repr__(self) -> str:
        from ui import Style

        return "\n\n".join(
            Style.set(f"{index + 1}:", Style.OKCYAN) + f" {tower}"
            for index, tower in enumerate(self.towers)
        )
