class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashMap= Counter(magazine)

        # a: 2
        # b :1

        for ch in ransomNote:
            if ch not in hashMap:
                return False
            else:
                hashMap[ch] -=1
                if hashMap[ch] == 0:
                    del hashMap[ch]
        return True


        