class LRUCache:
  def __init__(self, maxSize):
    self.maxSize = maxSize or 1
    self.size = 0
    self.map = {}
    self.linkHead = None
    self.linkTail = None

  def insertKeyValuePair(self, key, value):
    if key in self.map:
      self.map[key].value = value
      self.getValueFromKey(key)
      return

    node = DoubleLinkedList(key, value, None, self.linkHead)
    if self.linkHead:
      self.linkHead.prev = node
    self.linkHead = node
    self.map[key] = node
    if not self.linkTail:
      self.linkTail = node
    if self.size == self.maxSize:
      self.linkTail.prev.next = None
      self.map.pop(self.linkTail.key)
      self.linkTail = self.linkTail.prev
    else:
      self.size += 1

  def getValueFromKey(self, key):
    if key not in self.map:
      return None
    node = self.map[key]
    # Node has both next and prev
    if node.prev and node.next:
      node.prev.next = node.next
      node.next.prev = node.prev
      node.next = self.linkHead
      node.prev = None
      self.linkHead.prev = node
      self.linkHead = node
    # Node is the tail and not head
    elif node == self.linkTail and node != self.linkHead:
      self.linkTail = node.prev
      if node.prev.prev is None:
        node.prev.prev = node
      node.prev.next = None
      node.prev = None
      node.next = self.linkHead
      self.linkHead = node
    return node.value

  def getMostRecentKey(self):
    return self.linkHead.key

class DoubleLinkedList:
  def __init__(self, key, value, prev, nxt):
    self.prev = prev
    self.next = nxt
    self.value = value
    self.key = key

  def __repr__(self):
    return 'Node({0.key}->{0.value})'.format(self)

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
letterMap = {
    'a': 0,
    'b': 1,
    'c': 2,
    'd': 3,
    'e': 4,
    'f': 5,
    'g': 6,
    'h': 7,
    'i': 8,
    'j': 9,
}
import unittest
class LRUCacheTester(unittest.TestCase):
  def test_lru(self):
    for size in range(1, 11):
      lru = LRUCache(size)
      self.assertEqual(lru.getValueFromKey("a"), None)
      lru.insertKeyValuePair("a", 99)
      self.assertEqual(lru.getMostRecentKey(), "a")
      self.assertEqual(lru.getValueFromKey("a"), 99)
      lru.insertKeyValuePair("a", 0)
      self.assertEqual(lru.getMostRecentKey(), "a")
      self.assertEqual(lru.getValueFromKey("a"), 0)
      for i in range(1, size):
        mostRecentLetter = letters[i-1]
        self.assertEqual(lru.getMostRecentKey(), mostRecentLetter, 'size is {}, i is {}'.format(size, i))
        for j in range(i):
          letter = letters[j]
          self.assertEqual(lru.getValueFromKey(letter), letterMap[letter], 'size {}, i {}, j {}'.format(size, i, j))
          self.assertEqual(lru.getMostRecentKey(), letter)
        currentLetter = letters[i]
        self.assertEqual(lru.getValueFromKey(currentLetter), None)
        lru.insertKeyValuePair(currentLetter, letterMap[currentLetter])
        self.assertEqual(lru.getMostRecentKey(), currentLetter)
        self.assertEqual(lru.getValueFromKey(currentLetter), letterMap[currentLetter])

if __name__ == '__main__':
  unittest.main()