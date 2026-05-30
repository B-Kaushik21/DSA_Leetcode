class Solution:
    def minElement(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            s=str(nums[i])
            ans=0
            for j in range(len(s)):
                ans+=int(s[j])
            nums[i]=ans
        #print(nums)
        return min(nums)