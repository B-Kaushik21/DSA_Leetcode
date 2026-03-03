class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[-1]*n
        stk=[]
        for i in range(2*n):
            while stk and nums[stk[-1]]<nums[i%n]:
                res[stk.pop()]=nums[i%n]
            if i<n:
                stk.append(i)
        return res