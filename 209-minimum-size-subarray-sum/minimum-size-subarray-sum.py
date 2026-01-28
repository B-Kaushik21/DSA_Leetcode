class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if target==0:
            return 0
        n=len(nums)
        length=float('inf')
        i,j,summ=0,0,0
        while j<n:
            summ+=nums[j]
            while summ>=target:
                length=min(length,j-i+1)
                summ-=nums[i]
                i+=1
            j+=1
        return length if length!=float('inf') else 0