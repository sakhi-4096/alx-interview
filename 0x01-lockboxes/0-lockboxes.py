#!/usr/bin/python3
'''A module for working with lockboxes.'''


def canUnlockAll(boxes)->bool:
    '''Checks if all the boxes in a list of boxes can be unlocked
    given that the first box is unlocked.

    Args:
        boxes (list): A list of boxes where each box is represented by a list of integers.
    Returns:
        bool: True if all boxes can be unlocked, otherwise false.
    '''
    total_boxes = len(boxes)
    visited_boxes = {0}  # Set to keep track of visited boxes
    unvisited_boxes = set(boxes[0]) - {0}  # Set of boxes not yet visited

    while unvisited_boxes:
        current_box = unvisited_boxes.pop()

        # Check if the current box index is within valid range and not already visited
        if 0 <= current_box < total_boxes and current_box not in visited_boxes:
            unvisited_boxes.update(boxes[current_box])
            visited_boxes.add(current_box)

    return total_boxes == len(visited_boxes)
