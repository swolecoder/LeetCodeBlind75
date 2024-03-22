class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        parent = [ i for i in range(n)]
        logs.sort()
        def find(a):
            if parent[a] != a:
                parent[a] = find(parent[a])
            return parent[a]
        def union(a,b):
            A = find(a)
            B = find(b)

            if A != B:
                parent[B] = A
            
        def checker():
            check =  sum([ parent[i] == i for i in range(n)])
            print(check) 
            return check == 1
        

        for time, a,b in logs:
            union(a,b)
            if checker():
                return time
                # continue 
        
        return -1
        