from collections import defaultdict
class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        map = defaultdict(int)

        for frm, to, amount in transactions:
            map[frm] -= amount
            map[to] += amount
        print(map)

        debts = [amount for amount in map.values() if amount != 0]
        print(debts)
        

        def dfs(data):
            while data and data[0] == 0:
                data.pop(0)
            if not data:
                return 0

            
            count = float("inf")

            for i in range(1,len(data)):
                prev = data[0]

                if prev * data[i] < 0:
                    data[i] +=  data[0]
                    best = dfs(data[1:])
                    count = min(best, count)
                    # restore
                    data[i]-= data[0]
            return 1 + count 
        return dfs(debts)




        