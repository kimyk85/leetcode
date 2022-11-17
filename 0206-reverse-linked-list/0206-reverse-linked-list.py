# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tempList = []
        while head is not None:
            tempList.append(head.val)
            head = head.next

        tempList.reverse()
        tail = None
        for i, val in enumerate(tempList):
            if i == 0:
                tail = ListNode(val)
            else:
                cur = tail
                while cur.next is not None:
                    cur = cur.next
                cur.next = ListNode(val)

        return tail