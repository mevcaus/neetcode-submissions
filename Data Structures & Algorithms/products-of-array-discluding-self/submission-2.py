class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        left_total = 1
        right_total = 1
        res.append(1)
        for i in range(1, len(nums)):
            res.append(left_total * nums[i - 1])
            left_total *= nums[i - 1]
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= right_total
            right_total *= nums[i]
        return res