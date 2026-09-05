class ListNode:
    def __init__(self, key, prev=None, nxt=None):
        self.key = key
        self.prev = prev
        self.next = nxt


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.keyMap = {}

        self.head = ListNode(0)  # most recent side
        self.tail = ListNode(0)  # least recent side

        self.head.prev = self.tail
        self.tail.next = self.head

    def _add(self, key):
        node = ListNode(key)

        prev_node = self.head.prev
        prev_node.next = node

        node.prev = prev_node
        node.next = self.head

        self.head.prev = node

        return node

    def _remove(self, node):
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node

        return node

    def get(self, key: int) -> int:
        if key not in self.keyMap:
            return -1

        node, value = self.keyMap[key]

        self._remove(node)
        new_node = self._add(key)
        self.keyMap[key] = (new_node, value)

        return value

    def put(self, key: int, value: int) -> None:
        if key in self.keyMap:
            old_node, old_value = self.keyMap[key]
            self._remove(old_node)

        new_node = self._add(key)
        self.keyMap[key] = (new_node, value)

        if len(self.keyMap) > self.capacity:
            lru = self.tail.next
            self._remove(lru)
            del self.keyMap[lru.key]

