class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        triplets = []
        for index, num in enumerate(nums):
            if index > 0:
                if num == nums[index - 1]:
                    continue
            j = index + 1
            k = len(nums) - 1
            while j < k:
                total = num + nums[j] + nums[k]
                if total == 0:
                    triplets.append([num,nums[j],nums[k]])
                    j += 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                elif total > 0:
                    k -= 1
                else:
                    j += 1
        return triplets

                    