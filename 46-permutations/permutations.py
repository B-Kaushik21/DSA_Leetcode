class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # res=[]
        # n=len(nums)
        # def dfs(temp,used):
        #     if len(temp)==n:
        #         res.append(temp[:])
        #         return
        #     for i in range(n):
        #         if not used[i]:
        #             used[i]=True
        #             temp.append(nums[i])
        #             dfs(temp,used)
        #             temp.pop() #undo choice
        #             used[i]=False #mark as unused again
        # dfs([],[False]*n)
        # return res

        n=len(nums)
        res,sol=[],[]
        def backtrack():
            if len(sol)==n:
                res.append(sol[:])
                return 
            for x in nums:
                if x not in sol:
                    sol.append(x)
                    backtrack()
                    sol.pop()
        backtrack()
        return res