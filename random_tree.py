import random

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def generate():
    root = Node(0)

    if random.random() < 0.5:
        root.left = generate()
    if random.random() < 0.5:
        root.right = generate() 
    
    return root


class NodeLazy:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self._left = left
        self._right = right

        self._is_left_evaluated = False
        self._is_right_evaluated = False

    @property
    def left(self):
        if not self._is_left_evaluated:
            if random.random() < 0.5:
                self._left = Node(0)
        
        self._is_left_evaluated = True
        return self._left

    @property
    def right(self):
        if not self._is_right_evaluated:
            if random.random() < 0.5:
                self._right = Node(0)

        self._is_right_evaluated = True
        return self._right

def generate2():
    return NodeLazy(0)