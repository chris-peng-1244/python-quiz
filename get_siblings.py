class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def get_level(root, node, level=1):
    if not root:
        return 0
    if root == node:
        return level
    
    return get_level(root.left, node, level + 1) or \
        get_level(root.right, node, level + 1)

def get_cousins(root, node, level):
    if level <= 1:
        return []
    
    cousins = []
    if level == 2:
        if root.left != node and root.right != node:
            if root.left:
                cousins.append(root.left.data)
            if root.right:
                cousins.append(root.right.data)
    
    else:
        cousins += get_cousins(root.left, node, level - 1)
        cousins += get_cousins(root.right, node, level - 1)
    
    return cousins