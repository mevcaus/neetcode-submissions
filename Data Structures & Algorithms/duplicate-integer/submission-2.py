class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numhash = {}
        for num in nums:
            if num in numhash:
                return True
            else:
                numhash[num] = 0
        return False