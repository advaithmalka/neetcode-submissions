# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        curr1 = l1
        curr2 = l2

        head = ListNode()
        res = head
        while curr1 or curr2 or carry:
            s = carry
            if curr1:
                s += curr1.val
                curr1 = curr1.next
            if curr2:
                s += curr2.val
                curr2 = curr2.next

            carry = s // 10
            s = s % 10
            res.next = ListNode()
            res = res.next
            res.val = s

        return head.next