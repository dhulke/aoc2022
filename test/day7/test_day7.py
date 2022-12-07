import unittest

from day7.lib import File, Directory, Parser, Counter


class Day7TestCase(unittest.TestCase):
    def test_get_item(self):
        directory = Directory()
        inner_directory = Directory()
        directory.add_item("a", inner_directory)

        self.assertEqual(directory.get_item("a"), inner_directory)

    def test_get_parent(self):
        directory = Directory()
        inner_directory = Directory()
        directory.add_item("a", inner_directory)

        self.assertEqual(inner_directory.get_parent(), directory)

    def test_get_directories(self):
        directory_a = Directory()
        directory_b = Directory()
        directory_c = Directory()
        directory = Directory()
        directory.add_item("a", directory_a)
        directory.add_item("b", directory_b)
        directory.add_item("c", directory_c)
        directory.add_item("d", File(1))
        directory.add_item("e", File(2))

        self.assertEqual(len(directory.get_directories()), 3)
        self.assertTrue(directory_a in directory.get_directories())
        self.assertTrue(directory_b in directory.get_directories())
        self.assertTrue(directory_c in directory.get_directories())

    def test_file_size_is_consistent(self):
        file = File(123)

        self.assertEqual(file.size(), 123)

    def test_directory_size_with_one_file(self):
        directory = Directory()
        directory.add_item("a", File(123))

        self.assertEqual(directory.size(), 123)

    def test_directory_size_with_two_files(self):
        directory = Directory()
        directory.add_item("a", File(123))
        directory.add_item("b", File(7))

        self.assertEqual(directory.size(), 130)

    def test_inner_directories_with_files(self):
        directory = Directory()
        directory.add_item("a", File(123))
        directory.add_item("b", File(7))
        inner_directory = Directory()
        inner_directory.add_item("a", File(35))
        inner_directory.add_item("b", File(35))
        directory.add_item("c", inner_directory)

        self.assertEqual(directory.size(), 200)
        self.assertEqual(inner_directory.size(), 70)

    def test_parse_single_file(self):
        command_input = """$ cd /
$ ls
123 a"""
        directory = Parser.parse_input_commands(command_input)

        self.assertEqual(directory.size(), 123)

    def test_parse_multiple_files_and_directories(self):
        command_input = """$ cd /
$ ls
123 a
7 b
dir c
dir d
$ cd c
$ ls
30 a
30 b
$ cd ..
$ cd d
$ ls
5 a
5 b"""
        directory = Parser.parse_input_commands(command_input)

        self.assertEqual(directory.size(), 200)

    def test_parse_input_file(self):
        directory = Parser.parse_input_file("test/day7/small_input.txt")

        self.assertEqual(directory.size(), 200)

    def test_counter_size_100(self):
        directory = Parser.parse_input_file("test/day7/small_input.txt")
        self.assertEqual(Counter.sum_directory_sizes_below(directory, 100), 70);

    def test_counter_size_123(self):
        directory = Parser.parse_input_file("test/day7/small_input.txt")
        self.assertEqual(Counter.sum_directory_sizes_below(directory, 270), 270);

    def test_counter_size_10(self):
        directory = Parser.parse_input_file("test/day7/small_input.txt")
        self.assertEqual(Counter.sum_directory_sizes_below(directory, 15), 10);

    def test_least_directory_size_for_total_200_available_10(self):
        directory = Parser.parse_input_file("test/day7/small_input.txt")
        self.assertEqual(Counter.least_directory_size_to_available_space(directory, 200, 10), 10)

    def test_least_directory_size_for_total_200_available_50(self):
        directory = Parser.parse_input_file("test/day7/small_input.txt")
        self.assertEqual(Counter.least_directory_size_to_available_space(directory, 200, 50), 60)


if __name__ == '__main__':
    unittest.main()
