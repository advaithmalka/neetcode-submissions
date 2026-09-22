# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        secondHead = slow.next
        slow.next = None # split list
        prev = None 
        while secondHead:
            tmp = secondHead.next
            secondHead.next = prev
            prev = secondHead
            secondHead = tmp
        
        newHead = prev
        curr = head
        # merge
        while newHead:
            tmp1, tmp2 = curr.next, newHead.next
            curr.next = newHead
            newHead.next = tmp1
            curr = tmp1
            newHead = tmp2
        
        

