class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        s=str(n)
        freq=Counter(s)
        res=0
        for key,val in freq.items():
            res+=int(key)*val
        return res