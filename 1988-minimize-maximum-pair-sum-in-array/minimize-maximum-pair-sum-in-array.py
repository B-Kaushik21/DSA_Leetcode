class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        n=len(nums)
        l,r=0,n-1
        maxi=float('-inf')
        while l<r:
            temp=nums[l]+nums[r]
            maxi=max(maxi,temp)
            l+=1
            r-=1
        return maxi


