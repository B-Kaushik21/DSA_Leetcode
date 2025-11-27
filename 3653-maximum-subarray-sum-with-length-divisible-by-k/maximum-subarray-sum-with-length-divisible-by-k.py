class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        n=len(nums)
        mini=[inf]*(k-1)+[0]
        prefix,ans=0,-inf
        for i,x in enumerate(nums):
            prefix+=x
            ik=i%k
            ans=max(ans,prefix-mini[ik])
            mini[ik]=min(prefix,mini[ik])
        return ans