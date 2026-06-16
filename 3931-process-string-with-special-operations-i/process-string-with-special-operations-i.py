class Solution:
    def processStr(self, s: str) -> str:
        s=list(s)
        res=[]
        for ch in s:
            if ch in ['#','*','%']:
                if ch =='*':
                    if len(res)>=1:
                        res.pop()
                elif ch =='#':
                    res=res+res
                else:
                    res=res[::-1]
            else:
                res.append(ch)
        return ''.join(res)