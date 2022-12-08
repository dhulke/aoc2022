import unittest

from day8.lib import OutsideTreeViewer, Tree, OutsideTreeViewerFile, InsideTreeViewer, InsideTreeViewerFile


class Day8TestCase(unittest.TestCase):

    def test_outside_view_from_left_one_row(self):
        visible_trees = OutsideTreeViewer.from_left(row=0, trees=[[0, 1, 2, 3, 3]])
        expected = [Tree(0, 0), Tree(0, 1), Tree(0, 2), Tree(0, 3)]
        self.assertEqual(visible_trees, expected)

    def test_outside_view_from_left_two_rows(self):
        visible_trees = OutsideTreeViewer.from_left(row=1, trees=[[0, 1, 2, 3, 3], [4, 5, 3, 9, 9]])
        expected = [Tree(1, 0), Tree(1, 1), Tree(1, 3)]
        self.assertEqual(visible_trees, expected)

    def test_outside_view_from_right(self):
        visible_trees = OutsideTreeViewer.from_right(row=0, trees=[[0, 1, 2, 4, 3]])
        expected = [Tree(0, 4), Tree(0, 3)]
        self.assertEqual(visible_trees, expected)

    def test_outside_view_from_top(self):
        visible_trees = OutsideTreeViewer.from_top(column=0, trees=[[0], [1], [2], [3], [3]])
        expected = [Tree(0, 0), Tree(1, 0), Tree(2, 0), Tree(3, 0)]
        self.assertEqual(visible_trees, expected)

    def test_outside_view_from_bottom(self):
        visible_trees = OutsideTreeViewer.from_bottom(column=0, trees=[[0], [1], [2], [4], [3]])
        expected = [Tree(4, 0), Tree(3, 0)]
        self.assertEqual(visible_trees, expected)

    def test_outside_view_get_visible_trees(self):
        trees = [
            [3, 0, 3, 7, 3],
            [2, 5, 5, 1, 2],
            [6, 5, 3, 3, 2],
            [3, 3, 5, 4, 9],
            [3, 5, 3, 9, 0],
        ]

        self.assertEqual(OutsideTreeViewer.get_visible_trees(trees), 21)

    def test_outside_view_file_get_visible_trees(self):
        self.assertEqual(OutsideTreeViewerFile.get_visible_trees('test/day8/small_input.txt'), 21)

    def test_inside_view_from_left(self):
        self.assertEqual(InsideTreeViewer.from_left(0, 3, [[5, 5, 3, 4, 1]]), 2)

    def test_inside_view_from_left_to_edge(self):
        self.assertEqual(InsideTreeViewer.from_left(0, 3, [[0, 2, 3, 4, 1]]), 3)

    def test_inside_view_from_right(self):
        self.assertEqual(InsideTreeViewer.from_right(0, 1, [[0, 2, 1, 2, 2]]), 2)

    def test_inside_view_from_right_to_edge(self):
        self.assertEqual(InsideTreeViewer.from_right(0, 1, [[0, 2, 1, 0, 0]]), 3)

    def test_inside_view_from_top(self):
        self.assertEqual(InsideTreeViewer.from_top(3, 0, [[3], [3], [1], [3], [2]]), 2)

    def test_inside_view_from_top_to_edge(self):
        self.assertEqual(InsideTreeViewer.from_top(3, 0, [[0], [2], [1], [3], [2]]), 3)

    def test_inside_view_from_bottom(self):
        self.assertEqual(InsideTreeViewer.from_bottom(1, 0, [[3], [2], [1], [2], [2]]), 2)

    def test_inside_view_from_bottom_to_edge(self):
        self.assertEqual(InsideTreeViewer.from_bottom(1, 0, [[0], [2], [1], [0], [0]]), 3)

    def test_inside_view_get_scenic_score(self):
        trees = [
            [3, 0, 3, 7, 3],
            [2, 5, 5, 1, 2],
            [6, 5, 3, 3, 2],
            [3, 3, 5, 4, 9],
            [3, 5, 3, 9, 0],
        ]

        self.assertEqual(InsideTreeViewer.get_scenic_score(1, 2, trees), 4)
        self.assertEqual(InsideTreeViewer.get_scenic_score(3, 2, trees), 8)

    def test_inside_view_get_highest_scenic_score(self):
        trees = [
            [3, 0, 3, 7, 3],
            [2, 5, 5, 1, 2],
            [6, 5, 3, 3, 2],
            [3, 3, 5, 4, 9],
            [3, 5, 3, 9, 0],
        ]

        self.assertEqual(InsideTreeViewer.get_highest_scenic_score(trees), 8)

    def test_inside_view_file_get_highest_scenic_score(self):
        self.assertEqual(InsideTreeViewerFile.get_highest_scenic_score('test/day8/small_input.txt'), 8)


if __name__ == '__main__':
    unittest.main()
