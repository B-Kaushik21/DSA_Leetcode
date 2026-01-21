class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        res=[0]*len(nums)
        for i in range(len(nums)):
            for j in range(1,nums[i]):
                if (j | j+1) == nums[i]:
                    res[i]=j
                    break
                res[i]=-1
        return res
            