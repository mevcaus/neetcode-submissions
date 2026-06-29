class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement_hash = {}
        for index, num in enumerate(nums):
            if num in complement_hash:
                return [complement_hash[num], index]
            else:
                complement_hash[target - num] = index
        return []
        