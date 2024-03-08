class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        map = {
            "2": "abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz",
        }
        
        stack = []
        if not digits:
            return []
        res = []
        N = len(digits)
        stack.append((0, ""))
        while stack:
            local = []
            index, path = stack.pop()

            if index == N:
                res.append(path)
            if index <= N-1:
                for nei in map[digits[index]]:
                    stack.append((index+1,path + nei ))
        return res
        
        
    
        