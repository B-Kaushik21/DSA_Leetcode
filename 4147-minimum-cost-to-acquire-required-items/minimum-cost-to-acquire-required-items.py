class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        if need1==0 and need2==0:
            return 0
        ans=10**30
        x=0
        ans=min(ans,
                x*costBoth+
                need1*cost1+
                need2*cost2)
        x=min(need1,need2)
        ans=min(ans,
                x*costBoth+
                (need1-x)*cost1+
                (need2-x)*cost2)
        x=max(need1,need2)
        ans=min(ans,
                x*costBoth+
                max(0,need1-x)*cost1+
                max(0,need2-x)*cost2)
        return ans