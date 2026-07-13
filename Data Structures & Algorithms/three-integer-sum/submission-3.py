class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        sorted_nums = sorted(nums)
        for index,num in enumerate(sorted_nums):
            if index > 0 and num == sorted_nums[index - 1]:
                continue
            l,r = index + 1, len(nums) - 1
            while l < r:
                current_sum = num + sorted_nums[l] + sorted_nums[r]
                if current_sum == 0:
                    res.append([num, sorted_nums[l], sorted_nums[r]])
                    l += 1
                    r -= 1
                    while l < r and sorted_nums[l] == sorted_nums[l - 1]:
                        l += 1
                elif current_sum > 0:
                    r -= 1
                else:
                    l += 1
        return res