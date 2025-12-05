class Solution:
    def countElements(self, nums: List[int], k: int) -> int:
        if k==0:
            return len(nums)
        nums.sort()
        n=len(nums)
        
        threshold=nums[n-k]
        ans=0
        for num in nums:
            if num<threshold:
                ans+=1
        return ans