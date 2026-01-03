class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        temp=[]
        def dfs(idx,temp,res,n):
            if idx>=n:
                res.append(temp[:]) #copy current subsequence
                return
            #to pick
            temp.append(nums[idx])
            dfs(idx+1,temp,res,n)
            #backtrack(remove that index ele)
            temp.remove(nums[idx])
            #dont pick
            dfs(idx+1,temp,res,n)
        dfs(0,temp,res,len(nums))
        return res