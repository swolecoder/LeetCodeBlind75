class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        gratest = -1
        res = [0] * len(arr)

        for i in range(len(arr)-1,-1,-1):
            res[i] = gratest 

            gratest = max(gratest, arr[i])
        
        return res 


       