class Solution:
    def countTriples(self, n: int) -> int:
        count=0
        for i  in range(1,n):
            for j in range(i+1,n):
                s=math.sqrt(i*i+j*j)
                if s<=n and int(s)==s:
                    count+=2
        return count