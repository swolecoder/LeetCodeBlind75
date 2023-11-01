class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid
            # left part is sorted
            if nums[mid] > nums[r]:
                if nums[l] <= target <= nums[mid]:  # corrected this line
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] <= target <= nums[r]:  # corrected this line
                    l = mid + 1
                else:
                    r = mid - 1

        return -1

             



        