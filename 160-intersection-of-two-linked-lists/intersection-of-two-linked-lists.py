# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        def len(list):
            count = 0
            while list:
                count +=1
                list = list.next
            return count
        
        def moveX(list, forward):

            while forward:
                list = list.next
                forward -=1
            return list

        l1 = len(headA)
        l2 = len(headB)
        print(l1,l2)
        
        if l1 > l2:
            headA = moveX(headA, l1-l2)
        elif l1 < l2:
            headB = moveX(headB, l2-l1)
        

        while headA and headB:
            if headA == headB:
                return headA
            else:
                headA = headA.next
                headB = headB.next
        