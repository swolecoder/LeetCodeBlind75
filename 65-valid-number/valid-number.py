class Solution:
    def isNumber(self, s: str) -> bool:
        #["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"]

        digit,decimal, e, symbol = False, False, False, False

        for ch in s:
            if ch in "0123456789":
                digit = True
        
            elif ch in "+-":
                #"6+1"
                if symbol or digit or decimal:
                        return False
                symbol = True
            elif ch in ".":
                if decimal or e:
                    return False
                decimal = True

            elif ch in "eE":
                if not digit or e:
                    return False
                e = True
                digit = False
                symbol = False
                decimal = False
            else:

                return False
        return digit

        