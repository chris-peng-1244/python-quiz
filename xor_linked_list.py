class Node:
    def __init__(self, val):
        self.val = val
        self.both = 0


class XorLinkedList:
    def __init__(self):
        self.head: Node = None
        self.tail: Node = None
        self.__nodes = [] # This is to prevent garbage collection

    def add(self, node: Node):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.both = get_pointer(self.tail)
            self.tail.both = self.tail.both ^ get_pointer(node)
            self.tail = node
        # Without this line, Python thinks there is no way to reach between head and tail
        self.__nodes.append(node)

    def get(self, index: int):
        prev_id = 0
        node = self.head
        for i in range(index):
            next_id = prev_id ^ node.both

            if next_id:
                prev_id = id(node)
                node = _get_obj(next_id)
            else:
                raise IndexError("Linked list index out of range")
        return node
