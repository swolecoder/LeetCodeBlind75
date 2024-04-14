class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        start = sorted([interval[0] for interval in intervals])
        end  = sorted([interval[1] for interval in intervals])
        print(start)
        print(end)

        l = 0
        r = 0


        ans = 0
        room = 0


        while l < len(start) and r < len(end):

            cal = start[l] < end[r]
            if cal:
                room +=1
                l +=1
            else:
                room -=1
                r +=1
            
            ans = max(ans, room)
        return ans 


        