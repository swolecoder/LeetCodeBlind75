class Solution:
    def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:
        ans = []
        i =0
        j = 0

        while i < len(encoded1) and j < len(encoded2):

            val, freq = encoded1[i]
            val1,freq1 = encoded2[j]

            min_freq = min(freq,freq1)
            product = val * val1

            if not ans or ans[-1][0] != product:
                ans.append([product,min_freq])
            else:
                ans[-1][1] += min_freq
            
            encoded1[i][1] -=min_freq
            encoded2[j][1] -=min_freq

#if they are qual movre noth of them 
            if freq == min_freq:
                i +=1
            if freq1 == min_freq:
                j +=1
        return ans

        