import unittest
from copy import copy

from day9.lib import Position, is_adjacent, RopeMover, OneCharCommandRopeMoverParser


class Day9TestCase(unittest.TestCase):

    def test_is_adjacent(self):
        self.assertTrue(is_adjacent(Position(0, 0), Position(1, 1)))  # top right
        self.assertTrue(is_adjacent(Position(5, 5), Position(4, 6)))  # top left
        self.assertTrue(is_adjacent(Position(2, 3), Position(3, 2)))  # bottom right
        self.assertTrue(is_adjacent(Position(1, 4), Position(0, 3)))  # bottom left
        self.assertTrue(is_adjacent(Position(2, 4), Position(1, 4)))  # left
        self.assertTrue(is_adjacent(Position(10, 15), Position(11, 15)))  # right
        self.assertTrue(is_adjacent(Position(11, 15), Position(11, 16)))  # top
        self.assertTrue(is_adjacent(Position(11, 15), Position(11, 14)))  # bottom

        self.assertFalse(is_adjacent(Position(0, 0), Position(2, 0)))
        self.assertFalse(is_adjacent(Position(0, 0), Position(1, 2)))


    def test_get_tail_position_up_up_right_right(self):
        rope_mover = RopeMover()
        rope_mover.up()
        rope_mover.up()
        rope_mover.right()
        rope_mover.right()

        self.assertEqual(rope_mover.get_tail(), Position(1, 2))
        self.assertEqual(rope_mover.get_total_unique_tail_positions(), 3)

    def test_get_tail_position_site_example(self):
        rope_mover = RopeMover()
        for _ in range(4):
            rope_mover.right()
        for _ in range(4):
            rope_mover.up()
        for _ in range(3):
            rope_mover.left()
        rope_mover.down()
        for _ in range(4):
            rope_mover.right()
        rope_mover.down()
        for _ in range(5):
            rope_mover.left()
        for _ in range(2):
            rope_mover.right()

        self.assertEqual(rope_mover.get_tail(), Position(1, 2))
        self.assertEqual(rope_mover.get_total_unique_tail_positions(), 13)

    def test_one_char_command_rope_mover_parser(self):
        commands = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""
        rope_mover = OneCharCommandRopeMoverParser.newRopeMover(commands)

        self.assertEqual(rope_mover.get_tail(), Position(1, 2))
        self.assertEqual(rope_mover.get_total_unique_tail_positions(), 13)

    def test_moving_in_line_to_negative_x(self):
        commands = """L 4
R 4
L 4
R 4
L 4"""
        rope_mover = OneCharCommandRopeMoverParser.newRopeMover(commands)

        self.assertEqual(rope_mover.get_tail(), Position(-3, 0))
        self.assertEqual(rope_mover.get_total_unique_tail_positions(), 4)

    def test_moving_around(self):
        commands = """L 1
U 1
R 2
D 2
L 1
U 1"""
        rope_mover = OneCharCommandRopeMoverParser.newRopeMover(commands)

        self.assertEqual(rope_mover.get_tail(), Position(0, 0))
        self.assertEqual(rope_mover.get_total_unique_tail_positions(), 1)

    def test_one_char_command_rope_mover_parser_file(self):
        rope_mover = OneCharCommandRopeMoverParser.newRopeMoverFromFile('test/day9/small_input.txt')

        self.assertEqual(rope_mover.get_tail(), Position(1, 2))
        self.assertEqual(rope_mover.get_total_unique_tail_positions(), 13)


if __name__ == '__main__':
    unittest.main()
