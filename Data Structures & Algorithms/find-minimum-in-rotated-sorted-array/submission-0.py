class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0, len(nums) - 1
        min_num = float('inf')
        while l <= r:
            halfway = (l + r) // 2
            min_num = min(min_num, nums[halfway])
            if nums[halfway] < nums[r]:
                r = halfway
            else:
                l = halfway + 1
        return min_num