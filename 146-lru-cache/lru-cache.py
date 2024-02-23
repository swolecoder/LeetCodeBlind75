class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.next = None
        self.Prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.c = capacity
        self.cache = {}
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    # remove node from  list
    def delete(self,node):
        current = node
        nextNode = node.next
        prevNode = node.prev

        prevNode.next = nextNode
        nextNode.prev = prevNode


    
    #  add to right of list
    def insert(self, node):
        current = node
        # prev element from tal 
        prevElement = self.tail.prev

        prevElement.next = current
        current.prev = prevElement 
        current.next = self.tail
        self.tail.prev = current
        
        

    def get(self, key: int) -> int:

        if key in self.cache:
            # remmove from list 
            self.delete(self.cache[key])

            # add to right most position
            self.insert(self.cache[key])
            # move this to right
            return self.cache[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:

        if key in self.cache:
            self.delete(self.cache[key])
        # create a new Node with key and valuer
        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])

        if len(self.cache) > self.c:
            # delete or evict from left and del lru from cache, thats why we habe left pointer
            lru = self.head.next
            self.delete(lru)
            del self.cache[lru.key]



        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)