class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        longest = 0
        numset = set(nums)
        
        for num in numset:
            if num - 1 not in numset:
                current_length = 0
                while num in numset:
                    current_length += 1
                    num += 1
                longest = max(longest, current_length)
        return longest
                    



        