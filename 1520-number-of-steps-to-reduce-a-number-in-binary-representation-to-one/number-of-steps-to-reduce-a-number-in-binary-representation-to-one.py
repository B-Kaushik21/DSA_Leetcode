class Solution:
    def numSteps(self, s: str) -> int:
        count=0
        val=int(s,2)
        while val>1:
            if val%2:
                val+=1
            else:
                val>>=1
            count+=1
        return count