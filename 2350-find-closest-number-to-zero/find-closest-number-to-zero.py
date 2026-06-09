class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        res=0
        check=float('inf')
        for i in range(len(nums)):
            if abs(nums[i]-0)< check:
                res=nums[i]
                check=abs(nums[i]-0)
            elif abs(nums[i]-0)==check:
                res=max(res,nums[i])
        return res