from collections import Counter
from typing import List

class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        sticker_maps = [Counter(sticker) for sticker in stickers]
        memo = {}

        def dfs(remaining_target_str):
            if remaining_target_str in memo:
                return memo[remaining_target_str]
            if not remaining_target_str:
                return 0

            ans = float('inf')
            remaining_target_count = Counter(remaining_target_str)

            for sticker in sticker_maps:
               # Skip stickers that don't contribute to the target.
                # if remaining_target_str[0] not in sticker:
                #     continue
                if not any( ch in remaining_target_count for ch in sticker):
                    continue 

                # Attempt to use the sticker to reduce the target string.
                new_target_count = remaining_target_count - sticker
                
                new_target_str = ''.join(ch * new_target_count[ch] for ch in new_target_count)
                next_dfs = dfs(new_target_str)
                
                # if next_dfs != -1:
                ans = min(ans, 1 + next_dfs)

            memo[remaining_target_str] = ans
            return memo[remaining_target_str]
        
        # return dfs(target)
        call = dfs(target)
        return -1 if  call == float('inf') else call