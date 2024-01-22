class Solution:
    def reverseVowels(self, s: str) -> str:

        vowels = "aeiou"
        left = 0
        right = len(s)-1
        N = len(s)
        c = list(s)

        while left < right:
            while left < N and c[left].lower() not in vowels:
                left +=1
            while right >=0 and c[right].lower() not in vowels:
                right -=1
            if left < right:
                c[left], c[right] = c[right], c[left]
                left +=1
                right -=1
        return ''.join(c)
        