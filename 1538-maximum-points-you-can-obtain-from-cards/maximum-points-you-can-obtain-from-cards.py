class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        maxi=0
        n=len(cardPoints)
        #add from front
        for i in range(k):
            maxi+=cardPoints[i]
        curr=maxi

        for i in range(k-1,-1,-1):
            curr-=cardPoints[i]# remove front
            
            curr+=cardPoints[n-(k-i)] # add from end

            maxi=max(maxi,curr)

        return maxi