class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        numdict = {}
        longest = 0
        for num in nums:
            numdict[num] = 0
        
        for num in list(numdict.keys()):
            if num - 1 not in numdict:
                current_length = 0
                while num in numdict:
                    current_length += 1
                    num += 1
                longest = max(longest, current_length)
        return longest
                    



        