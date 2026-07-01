class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        longest = 1
        sorted_nums = sorted(nums)
        current_longest = 1
        for i in range(len(sorted_nums) - 1):
            if sorted_nums[i] == sorted_nums[i + 1]:
                continue
            if sorted_nums[i] + 1 != sorted_nums[i + 1]:
                longest = max(longest, current_longest)
                current_longest = 1
            else:
                current_longest += 1
        longest = max(longest, current_longest)
        return longest


        