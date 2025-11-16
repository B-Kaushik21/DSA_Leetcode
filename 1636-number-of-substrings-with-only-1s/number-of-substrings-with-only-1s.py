class Solution:
    def numSub(self, s: str) -> int:
        mod=10**9+7
        count=0
        total=0
        for a in s:
            if a=='1':
                count+=1
            else:
                count=0
            total=(total+count)%mod
        return total
            