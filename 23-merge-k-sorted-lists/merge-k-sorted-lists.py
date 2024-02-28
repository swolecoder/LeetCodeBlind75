# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        l = len(lists)
        if len(lists) == 0 or lists is None:
            return None


        while len(lists)  >1:
            merge_list = []
            for i in range(0,len(lists),2):
                l1 = lists[i]
                l2 = lists[i+1] if (i +1) < len(lists) else None

                merge_list.append(self.merge(l1,l2))
            lists = merge_list
        
        return lists[0]




    def merge(self,l1,l2):
        dummy = ListNode(-1)
        curr = dummy

        while l1 and l2:
            if l1.val < l2.val:
                curr.next = ListNode(l1.val)
                l1 = l1.next
            else:
                curr.next = ListNode(l2.val)
                l2 = l2.next 
            curr = curr.next

        if l1:
            curr.next = l1
        if l2:
            curr.next = l2
        return dummy.next
