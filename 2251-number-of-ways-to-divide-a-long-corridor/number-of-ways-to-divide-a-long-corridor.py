class Solution:
    def numberOfWays(self, corridor: str) -> int:
        res=1
        mod=10**9+7
        store=[i for i,c in enumerate(corridor) if c=='S']
        for i in range(1,len(store)-1,2):
            res=res*(store[i+1]-store[i])
        return res%mod * (len(store) %2==0 and len(store)>=2)
            