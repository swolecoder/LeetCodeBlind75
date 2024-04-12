class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:

        if arr[0] != 1:
            cal = arr[0] - 1
            if cal >= k:
                return k
            else:
                k -= cal
        

        i = 0 

        while i < len(arr) - 1:
            cal = arr[i+1] - arr[i]

            if cal != 1:
                
                for j in range(arr[i] +1 , arr[i+1]):
                    k -=1
                    if not k:
                        return j

            i +=1

        
        if k:
            return  arr[-1] + k



            