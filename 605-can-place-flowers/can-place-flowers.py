class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        f = [0] + flowerbed + [0]

        for i in range(1, len(f)-1):
            if not f[i-1] and not f[i] and not f[i+1] and n:
                f[i] = 1
                n -=1
                if n == 0:
                    break
        return n == 0
        