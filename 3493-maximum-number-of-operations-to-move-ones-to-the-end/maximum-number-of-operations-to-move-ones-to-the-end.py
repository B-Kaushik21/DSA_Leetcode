class Solution:
    def maxOperations(self, s: str) -> int:
        count_ones=0
        ops=0
        for i,char in enumerate(s):
            if char=='1':
                count_ones+=1
            elif i>0 and s[i-1]=='1':
                ops+=count_ones
        return ops
