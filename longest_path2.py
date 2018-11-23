from math import inf

class Node:
    def __init__(self, val, children=[]):
        self.val = val
        self.children = children

def longest_path(root):
    height, path = longest_height_and_path(root)
    return path

def longest_height_and_path(root):
    longest_path_so_far = -inf
    highest, second_highest = 0, 0
    for length, child in root.children:
        height, longest_path_length = longest_height_and_path(child)
        longest_path_so_far = max(longest_path_so_far, longest_path_length)

        if height + length > highest:
            highest, second_highest = height + length, highest
        elif height + length > second_highest:
            second_highest = height + length

    return highest, max(longest_path_so_far, highest + second_highest)