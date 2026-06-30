class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        suffix = 1
        prefixarr = []
        suffixarr = []
        for i in range(len(nums)):
            prefix = nums[i] * prefix
            prefixarr.append(prefix)
        i = len(nums) - 1
        while i >= 0:
            suffix = nums[i] * suffix
            suffixarr.append(suffix)
            i-=1
        suffixarr.reverse()
        res = []
        for i in range(len(nums)):
            if i == 0:
                res.append(suffixarr[i + 1])
            elif i == len(nums) - 1:
                res.append(prefixarr[i - 1])
            else:
                res.append(prefixarr[i - 1] * suffixarr[i + 1])
        return res
            
        

        