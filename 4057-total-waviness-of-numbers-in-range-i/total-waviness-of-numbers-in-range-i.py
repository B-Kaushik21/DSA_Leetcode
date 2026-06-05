class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        count=0
        for i in range(num1,num2+1):
            s=str(i)
            n=len(s)
            for j in range(1,n-1):
                if s[j-1]>s[j] and s[j]<s[j+1]:
                    count+=1
                elif s[j-1]<s[j] and s[j]>s[j+1]:
                    count+=1
        return count