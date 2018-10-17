def is_subtree(s, t):
    def is_equal(s, t):
        if s is None and t is None:
            return True
        if s is None or t is None:
            return False
        if s.val != t.val:
            return False
        return is_equal(s.left, t.left) and is_equal(s.right, t.right)

    if s is None:
        return False
    if is_equal(s, t):
        return True
    return is_subtree(s.left, t) or is_subtree(s.right, t) 

def is_subtree2(s, t):
    def preorder(root):
        traversal = []
        stack = [root]
        while stack:
            n = stack.pop()
            if n is None:
                # null marker
                traversal.append('.')
                continue
            else:
                traversal.append(str(n.val))
            stack.append(n.right)
            stack.append(n.left)
        return ',' + ','.join(traversal) + ','

    s_str = preorder(s)
    t_str = preorder(t)
    return t_str in s_str

class BinaryNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

root = BinaryNode(1, BinaryNode(2), BinaryNode(3, BinaryNode(4), BinaryNode(5)))
root2 = BinaryNode(3, BinaryNode(4), BinaryNode(5))

is_subtree2(root, root2)
