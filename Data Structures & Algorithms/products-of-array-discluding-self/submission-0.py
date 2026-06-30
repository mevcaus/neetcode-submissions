class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            current_total = 1
            for j in range(len(nums)):
                if i != j:
                    current_total *= nums[j]
            res.append(current_total)
        return res

        