class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        flower = [0] + flowerbed + [0]

        for i in range(1, len(flower)-1):
            if not flower[i-1]  and not flower[i] and not flower[i+1] and n > 0:
                flower[i] = 1
                n -=1
        print(flower)
        print(n)
        return n == 0
        