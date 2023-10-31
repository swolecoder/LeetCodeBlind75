class Solution:
    def minWindow(self, s: str, t: str) -> str:

        needM = Counter(t)
        haveM = {}
        ans = ""
        ansL = float("inf")
        need = len(needM)
        have = 0
        ans = ""
        ansL = float("inf")
        l = 0


        for r in range(len(s)):
            # keep increaing r until we have and eneed are met 
            haveM[s[r]] = haveM.get(s[r], 0) + 1
         
            if s[r] in needM and haveM[s[r]] == needM[s[r]]:
                have +=1
                

            while have == need:
                chr = s[l:r+1]
                if (r-l +1) < ansL:
                    print("Ashish")
                    ansL = r-l +1
                    ans = chr
                haveM[s[l]] = haveM[s[l]] -1

                if s[l] in needM and haveM[s[l]] < needM[s[l]]:
                    have -=1
                
                l +=1
        return ans
                
                
 
            

        # countT = Counter(t)
        # print(countT)
        # n = len(countT)
        # print("Ranjan", n)
        # ans = ""
        # l = float("inf")


        # def helper(str):
        #     print(str)
        #     for k, v in countT.items():
        #         print(k,v)
        #         if k not in str or str[k] < v:
        #             return False
        #     return True

        # for i in range(len(s)):
        #     for j in range(len(s)):
        #         word = s[i:j+1] 
        #         print(word)

        #         if helper(Counter(word)):
        #             if len(word)  < l:
        #                 ans = word
        #                 l = len(word)
        # return ans