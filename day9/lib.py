from collections import namedtuple
from typing import Set

Position = namedtuple('Position', 'x y')


def is_adjacent(position_a: Position, position_b: Position) -> bool:
    return (position_b.x - 1 <= position_a.x <= position_b.x + 1
            and position_b.y - 1 <= position_a.y <= position_b.y + 1)


class RopeMover:
    def __init__(self):
        self.__head: Position = Position(0, 0)
        self.__tail: Position = self.__head
        self.__unique_tail_positions: Set[Position] = {self.__tail}

    def up(self):
        previous_head = self.__head
        self.__head = Position(self.__head.x, self.__head.y + 1)
        self.__update_tail(previous_head)

    def right(self):
        previous_head = self.__head
        self.__head = Position(self.__head.x + 1, self.__head.y)
        self.__update_tail(previous_head)

    def down(self):
        previous_head = self.__head
        self.__head = Position(self.__head.x, self.__head.y - 1)
        self.__update_tail(previous_head)

    def left(self):
        previous_head = self.__head
        self.__head = Position(self.__head.x - 1, self.__head.y)
        self.__update_tail(previous_head)

    def __update_tail(self, previous_head):
        if not is_adjacent(self.__head, self.__tail):
            self.__tail = previous_head
            self.__unique_tail_positions.add(self.__tail)

    def get_tail(self):
        return self.__tail

    def get_total_unique_tail_positions(self):
        return len(self.__unique_tail_positions)


class OneCharCommandRopeMoverParser:
    @classmethod
    def newRopeMoverFromFile(cls, file_name: str) -> RopeMover:
        with open(file_name) as f:
            return cls.newRopeMover(f.read())

    @staticmethod
    def newRopeMover(commands: str) -> RopeMover:
        rope_mover = RopeMover()
        for command, times in map(lambda line: line.strip().split(' '), commands.splitlines()):
            if command == 'U':
                for _ in range(int(times)):
                    rope_mover.up()
            elif command == 'R':
                for _ in range(int(times)):
                    rope_mover.right()
            elif command == 'D':
                for _ in range(int(times)):
                    rope_mover.down()
            elif command == 'L':
                for _ in range(int(times)):
                    rope_mover.left()
        return rope_mover
