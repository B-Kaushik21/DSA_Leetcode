class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n=len(nums)
        prefix=[0]*(n+1)
    
        for i in range(n):
            prefix[i+1]=prefix[i]+(1 if nums[i]==target else -1)
        res=0
        print(prefix)
        for l in range(n):
            for r in range(l,n):
                if prefix[r+1]-prefix[l]>0:
                    res+=1
        return res