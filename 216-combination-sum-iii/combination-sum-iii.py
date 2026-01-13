class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res=[]
        def dfs(ind,path,target,k):
            if target==0 and k==0:
                res.append(path[:])
                return 
            for i in range(ind,10):
                if i>target and k<=0:
                    break
                path.append(i)
                dfs(i+1,path,target-i,k-1)
                path.pop()
        dfs(1,[],n,k)
        return res
