class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str: 

        l1, l2 = len(str1) , len(str2)

        def divisior(l):
            if l1 % l != 0 and l2 % l != 0:
                return False
            
            f1, f2 = l1 //l , l2 // l 
           #  Formal PROOF str1 + str2 == str2 + str1 Implies GCD Exists
            return str1[:l] * f1 == str1 and str2[:l] * f2 == str2 and str1+ str2 == str2 + str1
        

        for l in range(min(l1,l2), 0, -1):
            if divisior(l):
                return str1[:l]
        return ""
        