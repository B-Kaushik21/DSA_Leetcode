class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n=len(nums)
        maxi=-float(inf)
        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    maxi=max(maxi,(nums[i]-nums[j])*nums[k])
        return maxi if maxi>0 else 0