class Solution:
    def compress(self, chars: List[str]) -> int:
        i,r = 0, 0

        while i < len(chars):
            curr = chars[i]
            count = 0
            while i < len(chars) and curr == chars[i]:
                count +=1
                i +=1
            
            chars[r] = curr
            r +=1
            if count > 1:
                for d in str(count):
                    chars[r] = d
                    r +=1
      
        print(chars)
        return r

        