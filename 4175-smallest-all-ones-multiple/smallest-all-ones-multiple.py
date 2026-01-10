class Solution:
    def minAllOneMultiple(self, k: int) -> int:
        s=1
        n=1
        while s!=0:
            s=(s*10+1)%k
            n+=1
            if k%2==0 or k%5==0:
                return -1
        return n