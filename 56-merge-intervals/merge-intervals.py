class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        
        data = sorted(intervals, key=lambda x:x[0])
        res = [data[0]]

        for i in range(1,len(data)):

            curr = data[i]

            if res[-1][1] >= curr[0]:
                res[-1] = [min(res[-1][0], curr[0]), max(res[-1][1], curr[1])]
            else:
                res.append(curr)
        
        return res

        