class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:

        map1 = {}
        map2 = {}

        def dfs(i, j):

            if  i == len(pattern) and j == len(s):
                return True
            
            if i == len(pattern) or j == len(s):
                return False
            
            p_word = pattern[i]

            for index in range(j +1 , len(s)+1):
                s_word = s[j: index]


                # if p word and s word in 
                if p_word not in map1 and s_word not in map2:
                    map1[p_word] = s_word
                    map2[s_word] = p_word

                    if dfs(i+1, index) == True:
                        return True
                    # Backtrwack if not solution found 
                    del map1[p_word]
                    del map2[s_word]

                elif p_word  in map1 and map1[p_word] == s_word and  s_word  in map2 and map2[s_word] == p_word:
                    if dfs(i+1, index):
                        return True
            
            return False
        return dfs(0,0)


        # def backtrack(pat_index, s_index):
        #     # Base case: if both pattern and string are fully matched
        #     if pat_index == len(pattern) and s_index == len(s):
        #         return True
        #     if pat_index == len(pattern) or s_index == len(s):
        #         return False
            
        #     pat_char = pattern[pat_index]
            
        #     for end in range(s_index + 1, len(s) + 1):
        #         # Extracting the substring to match with current pattern character
        #         substr = s[s_index:end]
                
        #         # If the pattern character and substring have not been seen before
        #         if pat_char not in pattern_to_substring and substr not in used_substrings:
        #             pattern_to_substring[pat_char] = substr
        #             used_substrings.add(substr)
                    
        #             # Recur with the next parts of the pattern and string
        #             if backtrack(pat_index + 1, end):
        #                 return True
                    
        #             # Backtrack if no solution found along this path
        #             del pattern_to_substring[pat_char]
        #             used_substrings.remove(substr)
                
        #         # If this pattern character has been mapped before, check consistency and continue if it matches
        #         elif pat_char in pattern_to_substring and pattern_to_substring[pat_char] == substr:
        #             if backtrack(pat_index + 1, end):
        #                 return True
            
        #     return False
        
        # pattern_to_substring = {}
        # used_substrings = set()
        # return backtrack(0, 0)
