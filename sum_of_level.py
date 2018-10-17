from Queue import Queue
from collections import defaultdict

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def smallest_level(root):
    queue = Queue()
    queue.put((root, 0))
    level_to_sum = defaultdict(int) # Maps levels to its sum

    while not queue.empty():
        node, level = queue.get()
        level_to_sum[level] += node.value

        if node.right:
            queue.put((node.right, level + 1))

        if node.left:
            queue.put((node.left, level + 1))

    return min(level_to_sum, key=level_to_sum.get)


root1 = Node(
    value=1,
    left=Node(-2),
    right=Node(-3, Node(4), Node(-5))
)

print(smallest_level(root1))

root2 = Node(
    value=1,
    left=Node(2, Node(4), Node(5, Node(-1))),
    right=Node(
        value=3,
        right=Node(6, Node(-7), Node(-8))
    )
)
print(smallest_level(root2))