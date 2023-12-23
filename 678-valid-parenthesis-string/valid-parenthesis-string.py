class Solution:
    def checkValidString(self, s: str) -> bool:

        open = []
        star = []


        for i in range(len(s)):

            if s[i] == "(":
                open.append(i)
            elif s[i] == ")":
                if open:
                    open.pop()
                else:

                    if not open and not star:
                        return False
                    elif star:
                        star.pop()


            else:
                star.append(i)
        
        # balnce the open ones

        while open:
            if not star:
                return False
            
            o1 = open.pop()
            s1= star.pop()

            if o1 > s1:
                return False
        
        print(open, star)
        return True


        