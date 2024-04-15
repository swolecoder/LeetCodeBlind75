class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        hashMap =[Counter(sticker) for sticker in stickers]
        print(hashMap)

        memo = {}

        def helper(target_string, memo):
            if target_string in memo:
                return memo[target_string]
            
            if not target_string:
                return 0
            
            remaining = Counter(target_string)
            ans = float("inf")

            for data in hashMap:
                if not any( ch in remaining for ch in data):
                    continue
                
                left = remaining - data

                left_string = [ k * v for k,v in left.items()]
                ans = min(ans, 1+ helper(''.join(left_string), memo))
                # memo[target_string] = ans 
            
            memo[target_string] = ans
            return ans 
        
        data = helper(target, memo)
        print(data)
        if data == float("inf"):
            return -1
        return data


        