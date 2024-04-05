# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummyList = ListNode(-1)
        curr = dummyList

        carry  = 0

        while l1 or l2 or carry:

            total = (l1.val if l1 else 0) + ( l2.val if l2 else 0) + carry
            print(total)
            curr.next = ListNode(total % 10)
            carry = total // 10
           

            curr = curr.next

            l1 = l1 and l1.next
            l2 = l2 and l2.next
        
        return dummyList.next


        