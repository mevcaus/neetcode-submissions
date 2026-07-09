class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums) - 1
        while l <= r:
            halfway = (l + r) // 2
            if nums[halfway] == target:
                return halfway
            elif nums[l] <= nums[halfway]:
                if nums[l] <= target < nums[halfway]:
                    r = halfway - 1
                else:
                    l = halfway + 1
            else:
                if nums[halfway] < target <= nums[r]:
                    l = halfway + 1
                else:
                    r = halfway - 1
        return -1