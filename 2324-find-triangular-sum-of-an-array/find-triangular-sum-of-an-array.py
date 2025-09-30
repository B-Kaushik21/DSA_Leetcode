class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        k=len(nums)
        while k!=1:
            for i in range(k-1):
                nums[i]=(nums[i]+nums[i+1])%10
            k-=1
        return nums[0]