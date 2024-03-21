class ListNode:
    def __init__(self, key= None,val= None):
        self.key = key
        self.val = val
        self.next = None
class MyHashMap:

    def __init__(self):
        self.size = 1500
        self.hashmap = [None] * self.size
        
    def getHash(self, key):
        return key % self.size

    def put(self, key: int, value: int) -> None:
        hashKey = self.getHash(key)
        if self.hashmap[hashKey] is None:
            self.hashmap[hashKey] = ListNode(key, value)
        else:
            curr = self.hashmap[hashKey]
            while True:
                if curr.key == key:
                    curr.val = value
                    return
                if curr.next is None:
                    break
                curr = curr.next
            curr.next = ListNode(key, value)


        

    def get(self, key: int) -> int:
        hashKey = self.getHash(key)
        if self.hashmap[hashKey] is None:
            return -1
        else:
            curr = self.hashmap[hashKey] 
            while curr:
                if curr.key == key:
                    return curr.val
                
                curr = curr.next
        
        return -1



        

    def remove(self, key: int) -> None:
        hashKey = self.getHash(key)
        if self.hashmap[hashKey] is None:
            return 
        else:
            curr = self.hashmap[hashKey] 
            prev = None
            while curr:
                if curr.key == key:
                    if curr.next == None:
                        curr.key = None
                        curr.val = None
                    else:
                        curr.key = curr.next.key
                        curr.val = curr.next.val
                        curr.next = curr.next.next
                    
                    return 
                curr = curr.next
                prev = curr
        
        return -1

        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)