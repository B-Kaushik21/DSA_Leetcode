class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        close=float('-inf')
        for i in range(len(nums)-2):
            l,r=i+1,len(nums)-1
            while l<r:
                cur=nums[i]+nums[l]+nums[r]
                if abs(cur-target)<abs(close-target):
                    close=cur
                if cur<target:
                    l+=1
                elif cur>target:
                    r-=1
                else:
                    return cur
        return close
                
