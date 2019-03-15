# Feel free to add new properties and methods to the class.
class Node:
	def __init(self, value, prev=None, nxt=None):
		self.value = value
		self.prev = prev
		self.next = nxt


class DoublyLinkedList:
  def __init__(self):
    self.head = None
    self.tail = None

  def _moveToHead(self, node):
    node.prev.nxt = node.nxt
		node.prev = None
		self.head.prev = node
		node.nxt = self.head
		self.head = node

	def _addHead(self, node):
		node.prev = None
		node.nxt = self.head
		self.head.prev = node
		self.head = node

	def _moveToTail(self, node):
		node.prev.nxt = node.nxt
		node.nxt = None
		self.tail.nxt = node
		node.prev = self.tail
		self.tail = node

	def _addTail(self, node):
		node.nxt = None
		self.tail.nxt = node
		node.prev = self.tail
		self.tail = node

  def setHead(self, node):
    if self.containsNodeWithValue(node.value):
			self._moveToHead(node)
		else:
			self._addHead(node)

  def setTail(self, node):
    if self.containsNodeWithValue(node.value):
			self._moveToTail(node)
		else:
			self._addTail(node)

  def insertBefore(self, node, nodeToInsert):
		if nodeToInsert.prev:
			nodeToInsert.prev.nxt = node
		node.nxt = nodeToInsert
		nodeToInsert.prev = node

  def insertAfter(self, node, nodeToInsert):
    if nodeToInsert.nxt:
			nodeToInsert.nxt.prev = node
		node.prev = nodeToInsert
		nodeToInsert.nxt = node

  def insertAtPosition(self, position, nodeToInsert):
		if position <= 0:
			return

		position -= 1
    node = self.head
		while position:
			node = node.nxt
			position -= 1
		self.insertBefore(node)

  def removeNodesWithValue(self, value):
    node = self.head
		while node:
			if node.value == value:
				self.remove(node)
				break

  def remove(self, node):
		if node.prev:
      node.prev.nxt = node.nxt
		if node.nxt:
			node.nxt.prev = node.prev
		node = None

  def containsNodeWithValue(self, value):
		node = self.head
    	while node:
			if node.value == value:
				return True
			node = node.nxt
		return False
		
