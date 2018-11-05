def prune(node):
    if node is None:
        return None

    node.left, node.right = prune(node.left), prune(node.right)

    if node.left is None and node.right is None and node.val == 0:
        return None

    return node