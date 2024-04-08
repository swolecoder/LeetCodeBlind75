class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i, j = 0,0 

        while i < len(word) and j < len(abbr):
            if abbr[j].isdigit() and abbr[j] != '0':
                s = ""
                while j < len(abbr) and abbr[j].isdigit():
                    s += abbr[j]
                    j +=1
                
                i += int(s)
            else:
                if word[i] != abbr[j]:
                    return False
                
                i +=1
                j +=1
        return i == len(word) and j == len(abbr)
        