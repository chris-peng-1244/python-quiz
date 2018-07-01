class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(root: Node) -> str:
    if root is None:
        return '#'
    return '{} {} {}'.format(root.val, serialize(root.left), serialize(root.right))


def deserialize(data: str) -> Node:
    def helper():
        val = next(vals)
        if val == '#':
            return None
        node = Node(int(val))
        node.left = helper()
        node.right = helper()
        return node
    vals = iter(data.split())
    return helper()


root = Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6)))
sBTree = serialize(root)
print(sBTree)
deserRoot = deserialize(sBTree)
print(deserRoot)
