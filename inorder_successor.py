class Node:
    def __init__(self, val, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

def inorder_successor(node):
    if node.right:
        return leftmost(node.right)

    parent = node.parent

    while parent and parent.left is not node:
        parent, node = parent.parent, parent

    return parent

def leftmost(node):
    while node.left:
        node = node.left

    return node