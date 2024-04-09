class Solution:
    def intervalIntersection(self, first: List[List[int]], second: List[List[int]]) -> List[List[int]]:

        p1 , p2 = 0, 0
        output = []


        while p1 < len(first) and p2 < len(second):

            start = max(first[p1][0], second[p2][0])
            end = min(first[p1][1], second[p2][1])

            if start <= end:
                output.append([start, end])
            
            if first[p1][1] <= second[p2][1]:
                p1 +=1
            else:
                p2 +=1
        return output 



        