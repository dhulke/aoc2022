from day8.lib import TreePatch


if __name__ == '__main__':
    visible_trees = TreePatch.count_visible_trees_from_file("day8/actual_input.txt")

    assert visible_trees == 1688, "Answer to first part isn't correct"

    print(f"First part: {visible_trees}")