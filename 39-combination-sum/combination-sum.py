class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res,temp=[],[]
        def backtrack(ind,temp,res,target):
            if ind==len(candidates):
                if target==0:
                    res.append(temp[:])
                return 
            
            if candidates[ind]<=target:
                temp.append(candidates[ind])
                backtrack(ind,temp,res,target-candidates[ind])
                temp.pop()
            backtrack(ind+1,temp,res,target)
            return res
        return backtrack(0,temp,res,target)
        