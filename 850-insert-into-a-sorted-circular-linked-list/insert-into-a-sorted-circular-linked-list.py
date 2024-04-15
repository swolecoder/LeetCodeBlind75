"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':

        if not head:
            node = Node(insertVal)
            node.next = node
            return node
        
        curr = head

        while curr.next != head:

            if curr.val <= insertVal and insertVal <= curr.next.val:
                node = Node(insertVal)
                temp = curr.next
                curr.next = node
                node.next = temp
                
                return head
            
            elif curr.val > curr.next.val:
                if insertVal < curr.next.val or insertVal > curr.val:
                    node = Node(insertVal)
                    temp = curr.next
                    curr.next = node
                    node.next = temp
                    return head
            
            curr = curr and curr.next
        
        node = Node(insertVal,curr.next)
        curr.next = node
        # node.next = curr
        return head













