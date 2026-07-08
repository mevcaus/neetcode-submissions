class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums) - 1
        while l <= r:
            halfway = ((r + l) // 2)
            if nums[halfway] < target:
                l = halfway + 1
            elif nums[halfway] > target:
                r = halfway - 1
            else:
                return halfway
        return -1