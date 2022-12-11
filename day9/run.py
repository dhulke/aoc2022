from day9.lib import OneCharCommandRopeMoverParser


if __name__ == '__main__':

    rope_mover = OneCharCommandRopeMoverParser.newRopeMoverFromFile('day9/actual_input.txt')

    total_unique_tail_positions = rope_mover.get_total_unique_tail_positions()
    # assert visible_trees == 1688, "Answer to first part isn't correct"
    # assert scenic_score == 410400, "Answer to second part isn't correct"

    print(f"First part: {total_unique_tail_positions}")
    # print(f"Second part: {scenic_score}")