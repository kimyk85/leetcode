# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def returnListtonum(self, l: Optional[ListNode]) -> int:
        l_list = list()
        while l:
            l_list.append(str(l.val))
            l = l.next
        l_list.reverse()
        return int(''.join(l_list))
    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = self.returnListtonum(l1)
        num2 = self.returnListtonum(l2)
        print(num1, num2)
        num = num1 + num2
        numlist = list(str(num))
        numlist.reverse()

        print(numlist)
        r_list = ListNode(numlist[0])
        for v in numlist[1:]:
            cur = r_list
            while cur.next is not None:
                cur = cur.next
            cur.next = ListNode(v)
        return r_list