class Solution:
    def consecutiveSetBits(self, n: int) -> bool:
        s=bin(n)[2:]
        print(s)
        count=0
        pairs=0
        for i in range(1,len(s)):
            if s[i-1]=='1' and s[i]=='1':
                count+=1
                pairs+=1
            if pairs>1:
                return False
    
        #print(pairs)
        if pairs==1:
            return True
        return False
        