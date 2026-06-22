class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        b=a=l=o=n=0
        for t in text:
            if t=='b':
                b+=1
            elif t=='a':
                a+=1
            elif t=='l':
                l+=1
            elif t=='o':
                o+=1
            elif t=='n':
                n+=1
        return min(b,a,l//2,o//2,n)
