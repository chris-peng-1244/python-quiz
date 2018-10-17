class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

def two_sum(root, K):
    seen = {}

    for node in iter_tree(root):
        if K - node.val in seen:
            return (node, seen[K - node.val])
        seen[node.val] = node

    return Node

def iter_tree(root):
    if root:
        for node in iter_tree(root.left):
            yield node
        
        yield root

        for node in iter_tree(root.right):
            yield node

def two_sum2(root, K):
    for node_one in iter_tree(root):
        node_two = search(root, K - node_one.val)

        if node_two:
            return (node_one, node_two)

    return None

def search(node, val):
    if not node:
        return None

    if node.val == val:
        return node
    elif node.val < val:
        return search(node.right, val)
    else:
        return search(node.left, val)