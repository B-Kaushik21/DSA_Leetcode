class Solution:
    def compress(self, chars: List[str]) -> int:
        res,i=0,0
        while i<len(chars):
            letter=chars[i]
            count=0
            while i<len(chars) and chars[i]==letter:
                count+=1
                i+=1
            chars[res]=letter
            res+=1
            if count>1:
                for c in str(count):
                    chars[res]=c
                    res+=1
        return res