from typing import List
from collections import namedtuple


TreesHeights = List[List[int]]

Tree = namedtuple("Tree", "row column")


class OutsideTreeViewer:
    @staticmethod
    def from_left(row: int, trees: TreesHeights) -> List[Tree]:
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
    def from_right(row: int, trees: TreesHeights) -> List[Tree]:
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
    def from_top(column: int, trees: TreesHeights) -> List[Tree]:
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
    def from_bottom(column: int, trees: TreesHeights) -> List[Tree]:
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

    @classmethod
    def get_visible_trees(cls, trees: TreesHeights):
        visible_trees = set()
        for i in range(len(trees[0])):
            visible_trees.update(OutsideTreeViewer.from_left(i, trees))
            visible_trees.update(OutsideTreeViewer.from_right(i, trees))

        for i in range(len(trees)):
            visible_trees.update(OutsideTreeViewer.from_top(i, trees))
            visible_trees.update(OutsideTreeViewer.from_bottom(i, trees))

        return len(visible_trees)


class InsideTreeViewer:
    @staticmethod
    def from_left(row: int, column: int, trees: TreesHeights) -> int:
        tree_in_consideration = trees[row][column]
        score = 0
        for i in reversed(range(column)):
            score += 1
            if trees[row][i] >= tree_in_consideration:
                break
        return score

    @staticmethod
    def from_right(row: int, column: int, trees: TreesHeights) -> int:
        tree_in_consideration = trees[row][column]
        score = 0
        for i in range(column + 1, len(trees[row])):
            score += 1
            if trees[row][i] >= tree_in_consideration:
                break
        return score

    @staticmethod
    def from_top(row: int, column: int, trees: TreesHeights) -> int:
        tree_in_consideration = trees[row][column]
        score = 0
        for i in reversed(range(row)):
            score += 1
            if trees[i][column] >= tree_in_consideration:
                break
        return score

    @staticmethod
    def from_bottom(row: int, column: int, trees: TreesHeights) -> int:
        tree_in_consideration = trees[row][column]
        score = 0
        for i in range(row + 1, len(trees)):
            score += 1
            if trees[i][column] >= tree_in_consideration:
                break
        return score

    @classmethod
    def get_scenic_score(cls, row: int, column: int, trees: TreesHeights) -> int:
        return (cls.from_left(row, column, trees) *
                cls.from_right(row, column, trees) *
                cls.from_top(row, column, trees) *
                cls.from_bottom(row, column, trees))

    @classmethod
    def get_highest_scenic_score(cls, trees: TreesHeights) -> int:
        highest_scenic_score = 0
        for i in range(len(trees)):
            for j in range(len(trees[0])):
                if (scenic_score := cls.get_scenic_score(i, j, trees)) > highest_scenic_score:
                    highest_scenic_score = scenic_score
        return highest_scenic_score


class OutsideTreeViewerFile:
    @staticmethod
    def get_visible_trees(file_name: str) -> int:
        with open(file_name) as f:
            return OutsideTreeViewer.get_visible_trees(parse_trees_heights(f.read()))


class InsideTreeViewerFile:
    @staticmethod
    def get_highest_scenic_score(file_name: str):
        with open(file_name) as f:
            return InsideTreeViewer.get_highest_scenic_score(parse_trees_heights(f.read()))


def parse_trees_heights(trees: str) -> TreesHeights:
    return list(map(lambda line: list(map(int, list(line))), trees.splitlines()))
