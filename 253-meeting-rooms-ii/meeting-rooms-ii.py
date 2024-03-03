class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        start = sorted([interval[0] for interval in intervals])
        end = sorted([interval[1] for interval in intervals])

        res = 0

        print(start)
        print(end)

        s = 0
        e = 0
        count = 0

        while s < len(start):
            if start[s] < end[e]:
                count +=1
                s +=1
            else:
                count -=1
                e +=1
            res = max(res, count)

        return res
        