import unittest

from day8.lib import TreeViewer, Tree, TreePatch


class Day8TestCase(unittest.TestCase):

    def test_view_from_left_one_row(self):
        visible_trees = TreeViewer.from_left(row=0, trees=[[0, 1, 2, 3, 3]])
        expected = [Tree(0, 0), Tree(0, 1), Tree(0, 2), Tree(0, 3)]
        self.assertEqual(visible_trees, expected)

    def test_view_from_left_two_rows(self):
        visible_trees = TreeViewer.from_left(row=1, trees=[[0, 1, 2, 3, 3], [4, 5, 3, 9, 9]])
        expected = [Tree(1, 0), Tree(1, 1), Tree(1, 3)]
        self.assertEqual(visible_trees, expected)

    def test_view_from_right(self):
        visible_trees = TreeViewer.from_right(row=0, trees=[[0, 1, 2, 4, 3]])
        expected = [Tree(0, 4), Tree(0, 3)]
        self.assertEqual(visible_trees, expected)

    def test_view_from_top(self):
        visible_trees = TreeViewer.from_top(column=0, trees=[[0], [1], [2], [3], [3]])
        expected = [Tree(0, 0), Tree(1, 0), Tree(2, 0), Tree(3, 0)]
        self.assertEqual(visible_trees, expected)

    def test_view_from_bottom(self):
        visible_trees = TreeViewer.from_bottom(column=0, trees=[[0], [1], [2], [4], [3]])
        expected = [Tree(4, 0), Tree(3, 0)]
        self.assertEqual(visible_trees, expected)

    def test_tree_patch_count_visible_trees(self):
        trees = """30373
25512
65332
33549
35390"""
        self.assertEqual(TreePatch.count_visible_trees_from_string(trees), 21)

    def test_tree_patch_count_visible_trees_from_file(self):
        self.assertEqual(TreePatch.count_visible_trees_from_file('test/day8/small_input.txt'), 21)

if __name__ == '__main__':
    unittest.main()
