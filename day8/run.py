from day8.lib import parse_trees_heights, OutsideTreeViewer, InsideTreeViewer


if __name__ == '__main__':

    with open("day8/actual_input.txt") as f:
        trees = parse_trees_heights(f.read())

    visible_trees = OutsideTreeViewer.get_visible_trees(trees)
    scenic_score = InsideTreeViewer.get_highest_scenic_score(trees)

    assert visible_trees == 1688, "Answer to first part isn't correct"
    assert scenic_score == 410400, "Answer to second part isn't correct"

    print(f"First part: {visible_trees}")
    print(f"Second part: {scenic_score}")