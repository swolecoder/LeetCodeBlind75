class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """

        res = ""

        for word in strs:
            res += str(len(word)) + "#" + word
        print(res)
        return res
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        res = []

        i = 0
        while i < len(s):
            j = i
            while i < len(s) and s[i] != "#":
                i +=1
            
            # not i is pinting at # so get teh number 
            length = s[j :i]
            word_found = s[i +1 : i + int(length) +1]
            print(word_found)
            res.append(word_found)
            i = i + int(length)+1
        return res 
                
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))