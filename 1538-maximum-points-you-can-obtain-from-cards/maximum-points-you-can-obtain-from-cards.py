class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        res=0
        n=len(cardPoints)
        for i in range(k):
            res+=cardPoints[i]
        curr=res
        for i in range(k-1,-1,-1):
            curr-=cardPoints[i]
            curr+=cardPoints[n-k+i]

            res=max(res,curr)
        return res