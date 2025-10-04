class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxi=float('-inf')
        l=0
        r=len(height)-1
        while l<r:
            temp=min(height[l],height[r])*abs(l-r)
            maxi=max(maxi,temp)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return maxi