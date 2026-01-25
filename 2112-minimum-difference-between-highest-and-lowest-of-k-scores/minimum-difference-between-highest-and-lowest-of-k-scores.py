class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)
        mini=float('inf')
        l,r=0,k-1
        while r<len(nums):
            mini=min(mini,nums[l]-nums[r])
            l+=1
            r+=1
        return mini
