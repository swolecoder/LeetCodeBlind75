class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) -1

        while l < r:
            tar = numbers[l] + numbers[r]

            if tar < target:
                l +=1
            elif tar > target:
                r -=1
            else:
                return [l+1,r+1]
        