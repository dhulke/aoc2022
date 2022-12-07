from day7.lib import Parser, Counter


if __name__ == '__main__':
    directory = Parser.parse_input_file("day7/actual_input.txt")
    sum_directory_sizes = Counter.sum_directory_sizes_below(directory, 100000)
    available_space = Counter.least_directory_size_to_available_space(directory, 70000000, 30000000)
    print(f"First part: {sum_directory_sizes}")
    print(f"Second part: {available_space}")