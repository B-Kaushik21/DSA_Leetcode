class Solution:
    def isMiddleElementUnique(self, nums: list[int]) -> bool:
        n=len(nums)
        freq=Counter(nums)
        mid=nums[n//2]
        for key,val in freq.items():
            if key==mid and val==1:
                return True
        return False