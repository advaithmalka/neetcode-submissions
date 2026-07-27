# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or not lists[0]:
            return None

        res = []
        i = 0
        while len(lists) > 1:
            temp = []
            for i in range(0, len(lists), 2):
                if i + 1 == len(lists):
                    temp.append(self.mergeLists(lists[i], None))
                else:
                    temp.append(self.mergeLists(lists[i], lists[i+1]))
            lists = temp

        return lists[0]

    def mergeLists(self, l1, l2):
        head = ListNode()
        curr = head

        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next

        if l1:
            curr.next = l1
        if l2:
            curr.next = l2

        return head.next

        