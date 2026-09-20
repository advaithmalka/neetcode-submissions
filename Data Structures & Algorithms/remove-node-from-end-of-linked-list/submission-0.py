# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        length = 0
        while curr:
            length += 1
            curr = curr.next
        idxToRemove = length - n

        if idxToRemove == 0:
            return head.next
        prev = head
        idx = 0
        while idx < idxToRemove - 1 and prev:
            prev = prev.next
            idx += 1

        
        if prev.next:
            prev.next = prev.next.next

        return head