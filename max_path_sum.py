def max_path_sum(tree):
    max_sum_branch, runtime_max_sum = max_path_sum_helper(tree)
    return max(max_sum_branch, runtime_max_sum)

def max_path_sum_helper(tree):
    if not tree:
        return (0, 0)

    left_sum_branch, left_sum = max_path_sum_helper(tree.left)
    right_sum_branch, right_sum = max_path_sum_helper(tree.right)
    max_child_sum_branch = max(left_sum_branch, right_sum_branch)
    max_sum_branch = max(max_child_sum_branch + tree.value, tree.value)
    max_sum = max(max_sum_branch, left_sum_branch + tree.value + right_sum_branch)
    runtime_max_sum = max(left_sum, right_sum, max_sum)
    return max_sum_branch, runtime_max_sum


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, values, i=0):
        if i >= len(values):
            return
        queue = [self]
        while len(queue) > 0:
            current = queue.pop(0)
            if current.left is None:
                current.left = BinaryTree(values[i])
                break
            queue.append(current.left)
            if current.right is None:
                current.right = BinaryTree(values[i])
                break
            queue.append(current.right)
        self.insert(values, i + 1)
        return self


# tree1 = BinaryTree(1).insert([2, 3, 4, 5, 6, 7])
# print(max_path_sum(tree1))

tree2 = BinaryTree(1).insert([2, 3])
print(max_path_sum(tree2))
