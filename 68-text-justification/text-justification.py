class Solution:
    def fullJustify(self, word: List[str], maxWidth: int) -> List[str]:

        res = []
        curr = []
        width = 0
        i = 0

        while i < len(word):

            if  width + len(word[i]) <= maxWidth:
                curr.append(word[i])
                width += len(word[i]) +1
                i +=1
            else:
                space = maxWidth - width + len(curr) # First this is in an example - > 16 - 11 + 3 -> 8 extra spaces bec we already added wifth +1
                print(space, width)
                added = 0 # keep a track of how many we added 
                j = 0  # llop through curr 
                #don't want to add spaces on last one
                while  added < space:
                    if j >=len(curr)-1:
                        j = 0
                    curr[j] += " "
                    added +=1
                    j +=1

                res.append(''.join(curr))
                curr = []
                width = 0

        # print(width, curr)   15 ['justification.']
        print(res)                
        for  i in range(len(curr) -1):
            curr[i] += " "
        curr[-1]  += " "* (maxWidth - width +1)

        res.append(''.join(curr))
        return res           