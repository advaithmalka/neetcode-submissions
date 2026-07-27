class ListNode:
    def __init__(self, key = 0, val = 0):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.right = ListNode()
        self.left = ListNode()
        self.right.prev, self.left.next = self.left, self.right

    def _insert(self, node):
        self.right.prev.next = node
        node.prev = self.right.prev
        node.next = self.right
        self.right.prev = node

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        
    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._insert(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].val = value
            self._remove(self.cache[key])
        else:
            self.cache[key] = ListNode(key, value)
        self._insert(self.cache[key])
        
        if len(self.cache) > self.capacity:
            lru = self.left.next
            self._remove(lru)
            del self.cache[lru.key]


