from typing import List
from collections import namedtuple


Tree = namedtuple("Tree", "row column")


class TreeViewer:
    @staticmethod
    def from_left(row: int, trees: List[List[int]]) -> List[Tree]:
        trees_in_row = len(trees[row])
        assert trees_in_row, f"There are no trees in row {row}"

        previous_tallest_tree = trees[row][0]
        visible_trees = [Tree(row, 0)]

        for i in range(1, trees_in_row):
            if previous_tallest_tree < trees[row][i]:
                previous_tallest_tree = trees[row][i]
                visible_trees.append(Tree(row, i))
                if previous_tallest_tree == 9:
                    break
        return visible_trees

    @staticmethod
    def from_right(row: int, trees: List[List[int]]) -> List[Tree]:
        trees_in_row = len(trees[row])
        assert trees_in_row, f"There are no trees in row {row}"

        previous_tallest_tree = trees[row][trees_in_row - 1]
        visible_trees = [Tree(row, trees_in_row - 1)]

        for i in reversed(range(1, trees_in_row)):
            if previous_tallest_tree < trees[row][i]:
                previous_tallest_tree = trees[row][i]
                visible_trees.append(Tree(row, i))
                if previous_tallest_tree == 9:
                    break
        return visible_trees

    @staticmethod
    def from_top(column: int, trees: List[List[int]]) -> List[Tree]:
        trees_in_column = len(trees)
        assert trees_in_column, f"There are no trees in a column"

        previous_tallest_tree = trees[0][column]
        visible_trees = [Tree(0, column)]

        for i in range(1, trees_in_column):
            if previous_tallest_tree < trees[i][column]:
                previous_tallest_tree = trees[i][column]
                visible_trees.append(Tree(i, column))
                if previous_tallest_tree == 9:
                    break
        return visible_trees

    @staticmethod
    def from_bottom(column: int, trees: List[List[int]]) -> List[Tree]:
        trees_in_column = len(trees)
        assert trees_in_column, f"There are no trees in a column"

        previous_tallest_tree = trees[trees_in_column - 1][column]
        visible_trees = [Tree(trees_in_column - 1, column)]

        for i in reversed(range(1, trees_in_column)):
            if previous_tallest_tree < trees[i][column]:
                previous_tallest_tree = trees[i][column]
                visible_trees.append(Tree(i, column))
                if previous_tallest_tree == 9:
                    break
        return visible_trees


class TreePatch:

    @classmethod
    def count_visible_trees_from_file(cls, file_name: str) -> int:
        with open(file_name) as f:
            return cls.count_visible_trees_from_string(f.read())

    @staticmethod
    def count_visible_trees_from_string(trees: str) -> int:
        trees_heights = list(map(lambda line: list(map(int, list(line))), trees.splitlines()))
        visible_trees = set()
        for i in range(len(trees_heights[0])):
            visible_trees.update(TreeViewer.from_left(i, trees_heights))
            visible_trees.update(TreeViewer.from_right(i, trees_heights))

        for i in range(len(trees_heights)):
            visible_trees.update(TreeViewer.from_top(i, trees_heights))
            visible_trees.update(TreeViewer.from_bottom(i, trees_heights))

        return len(visible_trees)
