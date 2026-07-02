class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        complement_hash = {}
        for index, num in enumerate(numbers):
            if num in complement_hash:
                return [complement_hash[num] + 1, index + 1]
            complement_hash[target-num] = index
        return []
        