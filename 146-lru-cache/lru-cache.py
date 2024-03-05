class DLL:
    def __init__(self,key,val,left=None,prev=None):
        self.key = key
        self.val = val
        self.left = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}
        self.head = DLL(-1,-1)
        self.tail = DLL(-1,-1)
        self.head.next =self.tail
        self.tail.prev = self.head
        
    def insert(self, node):
        current = node
        # prev element from tal 
        prevElement = self.tail.prev

        prevElement.next = current
        current.prev = prevElement 
        current.next = self.tail
        self.tail.prev = current

    
    def delete(self,node):
        prev = node.prev
        nextNode = node.next

        prev.next = nextNode
        nextNode.prev = prev

    def get(self, key: int) -> int:
        if key in self.map:
            # delete 
            node = self.map[key]
            self.delete(node)
            self.insert(node)
            return self.map[key].val
        return -1
            
        

    def put(self, key: int, value: int) -> None:

        if key in self.map:
            self.delete(self.map[key])
        
        self.map[key] = DLL(key,value)
        self.insert(self.map[key])

        if len(self.map) > self.capacity:
            lru = self.head.next
            self.delete(lru)
            del self.map[lru.key]
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)