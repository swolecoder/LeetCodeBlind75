class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not  intervals:
            return []
        
        data = sorted(intervals, key=lambda x: x[0])
        print(data)


        res  = [data[0]]

        for i in range(1, len(data)):
            curr = data[i]

            prev = res[-1]
            if prev[1] >= curr[0]:
                prev[-1] = max(curr[-1], prev[-1])
            else:
                res.append(curr)
        return res 
        