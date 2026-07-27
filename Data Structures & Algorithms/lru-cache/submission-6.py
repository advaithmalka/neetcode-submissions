class ListNode:
    def __init__(self, key, value=0):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left = ListNode(0,0)
        self.right = ListNode(0,0)

        self.left.next, self.right.prev = self.right, self.left

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = node.next = None
    
    def _add(self, node):
        self.right.prev.next = node
        node.prev = self.right.prev
        node.next = self.right
        self.right.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._remove(node)
        else:
            node = ListNode(key, value)
            self.cache[key] = node
        
        self._add(node)

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self._remove(lru)
            del self.cache[lru.key]

        
