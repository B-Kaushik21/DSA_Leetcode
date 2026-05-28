class Solution:
    def validDigit(self, n: int, x: int) -> bool:
        s=str(n)
        count=0
        if s[0]==str(x):
            return False
        for i in range(1,len(s)):
            if s[i]==str(x):
                count+=1
        if count>=1:
            return True
        return False