class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        text=list(text)
        res=0
        while True:
            word=list('balloon')
            for ch in word:
                found=False
                for i in range(len(text)):
                    if text[i]==ch:
                        text[i]='*'
                        found=True
                        break
                if not found:
                    return res
            res=res+1
