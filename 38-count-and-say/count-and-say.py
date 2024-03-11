class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        
        prev = self.countAndSay(n-1)
        res = ""
        
        count = 1
        for i in range(len(prev)):
            # Check if it's the last character or the current character is different from the next one
            if i == len(prev) - 1 or prev[i] != prev[i+1]:
                # Append the count and the current character to the result
                res += str(count) + prev[i]
                # Reset the count for the next character
                count = 1
            else:
                # Increment count if the current character is the same as the next one
                count += 1
        
        return res



        