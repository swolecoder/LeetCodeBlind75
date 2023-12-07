class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

      word = s.split()

      patternH = {}
      wordH = {}

      if len(pattern) != len(word):
        return False


      for p, w in zip(pattern , word):

        if p in patternH and patternH[p] != w:
          return False
        
        if w in wordH and wordH[w] != p:
          return False

        patternH[p] = w
        wordH[w] = p  



      return True      