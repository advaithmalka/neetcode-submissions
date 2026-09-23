"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToNew = {None:None}
        curr = head
        while curr:
            copyNode = Node(curr.val, None, None)
            oldToNew[curr] = copyNode
            curr = curr.next

        curr = head
        while curr:
            newNode = oldToNew[curr]
            newNode.next = oldToNew[curr.next]
            newNode.random = oldToNew[curr.random]
            curr = curr.next
        return oldToNew[head]