class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None
        
class LRUCache:

    # {key:value}
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # nodes
        
        # doubly linked list
        self.start, self.end = Node(0,0), Node(0,0)
        self.start.next, self.end.prev = self.end, self.start

    def remove(self, node):
        node.prev.next, node.next.prev = node.next, node.prev

    def insert_right(self, node):
        node.next, node.prev = self.end, self.end.prev
        node.prev.next = self.end.prev = node


    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert_right(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])

        newNode = Node(key,value)
        self.cache[key] = newNode
        self.insert_right(newNode)
        
        if len(self.cache) > self.capacity:
            lru_key = self.start.next.key
            self.remove(self.start.next)
            del self.cache[lru_key]

