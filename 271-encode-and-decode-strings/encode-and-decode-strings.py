class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """

        res = ""

        for strs in strs:
            res += str(len(strs)) + "#"+ strs
        return res
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """

        res , i = [], 0
        print(s)
        while i < len(s):

            j = i 
            print(i)
            while s[j] != "#" and j < len(s):
                j +=1
            length = int(s[i:j])
            res.append(s[j+1 : j+1 + length])
            i = j + length +1
        
        return res
            

        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))