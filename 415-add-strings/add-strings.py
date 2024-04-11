class Solution:
    def addStrings(self, num1: str, num2: str) -> str:

        i, j = len(num1)-1, len(num2)-1

        ans = ""
        carry = 0


        while i >=0 or j >=0 or carry:

            running_sum = 0

            if num1[i] and i >=0:

                running_sum += ord(num1[i])- 48

                i -=1
            
            if num2[j] and j >=0:

                running_sum += ord(num2[j])- 48

                j -=1
            

            running_sum += carry 
            ans = str(running_sum % 10) + ans

            carry = running_sum //10
        
        if carry > 0 :
            ans = "1" + ans
        
        return ans
        