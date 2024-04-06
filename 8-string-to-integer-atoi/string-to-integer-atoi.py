class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()

        if not s:
            return 0

        negative = False
        i = 0
        if s and s[i] == "+" or s[i] == "-":
            negative = s[i] == "-"
            i +=1
        
     
        
        parse = 0
        while i < len(s):
            if s[i].isdigit():
                parse = parse * 10 + int(s[i])
                i +=1
            else:
                break
        
        print(parse)
        if negative:
            parse = -1 * parse

        if parse > pow(2, 31) -1:
            return pow(2, 31) -1
        if parse < -1*pow(2, 31):
            return -1*pow(2, 31)
        return  parse


            



        