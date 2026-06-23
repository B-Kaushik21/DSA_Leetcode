class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        dp=Counter([0])
        for num in nums:
            for k,v in list(dp.items()):
                dp[k|num]+=v
        return dp[max(dp)]
                