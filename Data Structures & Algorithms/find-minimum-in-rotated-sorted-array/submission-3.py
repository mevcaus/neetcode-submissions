class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0, len(nums) - 1
        min_num = float('inf')
        while l <= r:
            m = (l + r) // 2
            if nums[l] <= nums[m]:
                min_num = min(min_num, nums[l])
                l = m + 1
            else:
                min_num = min(min_num, nums[m])
                r = m - 1
        return min_num