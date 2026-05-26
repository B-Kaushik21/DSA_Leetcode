class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lower='abcdefghijklmnopqrstuvwxyz'
        #upper='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        #print(chr(99-32))
        words=''
        for w in word:
            if w not in words:
                words+=w
        
        res=0
        for w in words:
            if w in lower:
                s=chr(ord(w)-32)
                if s in words:
                    res+=1
        return res
        