class Solution:
    def validate(self, s):
        if not s:
            return False
        digit_seen = False
        sign_seen = False

        i = 0 
        if s[i] in ["+","-"]:
            i +=1
        
        while i < len(s):
            if s[i] in ["+", "-"]:
                return False
            else:
                if not s[i].isdigit():
                    return False
                digit_seen= True
            i +=1
        return digit_seen
    def isNumber(self, s: str) -> bool:
        # ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"]

        decimal_seen = False
        digit_seen = False
        sign_seen = False
        i = 0
        if s[i] in ["+","-"]:
            i +=1
            sign_seen = True
        
        while i < len(s):
            if s[i] in ["E", "e"]:
                if not digit_seen:
                    return False
                else:
                    return digit_seen and  self.validate(s[i+1:])
            elif s[i] in ["+","-"]:
                if sign_seen or digit_seen or decimal_seen:
                    return False
            elif s[i] == ".":
                if  decimal_seen:
                    return False
                else:
                    decimal_seen = True
            else:
                if not s[i].isdigit():
                    return False
                digit_seen = True
            i +=1

        return digit_seen