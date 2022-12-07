from functools import reduce
from abc import ABC, abstractmethod
from typing import Dict, List, cast


class FileSystemItem(ABC):
    @abstractmethod
    def size(self):
        pass


class File(FileSystemItem):
    def __init__(self, size: int):
        self.__size = size

    def size(self) -> int:
        return self.__size


class Directory(FileSystemItem):
    def __init__(self):
        self.__items: Dict[str, FileSystemItem] = {}
        self.__parent: Directory

    def get_item(self, name: str) -> FileSystemItem:
        return self.__items[name]

    def get_parent(self) -> "Directory":
        return self.__parent

    def get_directories(self) -> List["Directory"]:
        return cast(List[Directory], list(filter(lambda item: isinstance(item, Directory), self.__items.values())))

    def add_item(self, name: str, item: FileSystemItem) -> None:
        self.__items[name] = item
        if isinstance(item, Directory):
            item.__set_parent(self)

    def __set_parent(self, directory: "Directory"):
        self.__parent = directory

    def size(self):
        return reduce(lambda acc, c: acc + c.size(), self.__items.values(), 0)


class Parser:

    @staticmethod
    def parse_input_commands(input_commands: str) -> Directory:
        return Parser(input_commands).parse()

    @classmethod
    def parse_input_file(cls, file_name: str) -> Directory:
        with open(file_name) as f:
            return cls.parse_input_commands(f.read())

    def __init__(self, input_commands: str):
        self.__input_commands = input_commands
        self.__root_directory = Directory()
        self.__current_directory: Directory

    def parse(self) -> Directory:
        for line in self.__input_commands.splitlines():
            if self.__is_command(line):
                self.__run_command(line)
            else:
                self.__add_item(line)
        return self.__root_directory

    @staticmethod
    def __is_command(line):
        return line.startswith("$")

    def __run_command(self, line):
        if line.startswith("$ cd .."):
            self.__current_directory = self.__current_directory.get_parent()
            assert self.__current_directory, "Cannot go above root"
        elif line.startswith("$ cd /"):
            self.__current_directory = self.__root_directory
        elif not line.startswith("$ ls"):
            # lazy way of checking it's a cd command
            directory_name = line[5:].strip()
            self.__current_directory = self.__current_directory.get_item(directory_name)

    def __add_item(self, line):
        if line.startswith("dir"):
            self.__current_directory.add_item(line[4:].strip(), Directory())
        else:
            size, name = line.strip().split()
            self.__current_directory.add_item(name, File(int(size)))


class Counter:
    @classmethod
    def sum_directory_sizes_below(cls, directory: Directory, size: int) -> int:
        count = cls.__recursive_count(directory, size)
        directory_size = directory.size()
        if directory_size <= size:
            count += directory_size
        return count

    @classmethod
    def __recursive_count(cls, directory: Directory, size: int) -> int:
        directories = directory.get_directories()
        count = reduce(lambda acc, c: acc + (c if c <= size else 0),
                       map(lambda d: d.size(), directories), 0)
        for directory in directories:
            count += cls.__recursive_count(directory, size)
        return count

    @classmethod
    def least_directory_size_to_available_space(cls,
                                                directory: Directory,
                                                total_space: int,
                                                expected_available_space: int) -> int:
        used_space = directory.size()
        available_space = total_space - used_space
        needed_space = expected_available_space - available_space
        sizes = cls.__directory_sizes(directory)
        sizes.append(directory.size())
        for size in sorted(sizes):
            if size >= needed_space:
                return size

    @classmethod
    def __directory_sizes(cls, directory: Directory) -> List[int]:
        sizes = []
        for directory in directory.get_directories():
            sizes.append(directory.size())
            sizes.extend(cls.__directory_sizes(directory))
        return sizes
