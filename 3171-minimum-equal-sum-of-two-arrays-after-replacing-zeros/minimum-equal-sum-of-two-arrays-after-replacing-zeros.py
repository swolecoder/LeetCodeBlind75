class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        sum1 = sum(nums1)
        count1 = nums1.count(0)
        total1 = sum1 + count1


        sum2= sum(nums2)
        count2 = nums2.count(0)
        total2 = sum2 + count2

        print(sum1, count1,sum2, count2)

        if total1 > total2:
            return total1 if count2 else -1
        elif total1 < total2:
            return total2 if count1 else -1
        else:
            return total1
        