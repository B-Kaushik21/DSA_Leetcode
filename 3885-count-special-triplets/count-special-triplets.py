class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        count=0
        left,right=Counter(),Counter(nums)
        
        for num in nums:
            right[num]-=1
            count+=left[num*2]*right[num*2]
            left[num]+=1
    
        return count%(10**9+7)