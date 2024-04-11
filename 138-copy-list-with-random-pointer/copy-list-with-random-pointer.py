"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if not head:
            return None

        map = {}
        map[head] = Node(head.val)


        present = head

        while head:
            if head.next and head.next not in map:
                map[head.next] = Node(head.next.val)
            
            map[head].next = map.get(head.next, None)


            if head.random and head.random not in map:
                map[head.random] = Node(head.random.val)
            map[head].random = map.get(head.random, None)


            head = head.next
        
        return map[present]
        