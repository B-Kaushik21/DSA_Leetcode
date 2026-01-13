class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]

        def findSubsets(ind,ds,res):
            res.append(ds[:])
            for i in range(ind,len(nums)):
                if i>ind and nums[i]==nums[i-1]:
                    continue
                ds.append(nums[i])
                findSubsets(i+1,ds,res)
                ds.pop()
        findSubsets(0,[],res)
        return res