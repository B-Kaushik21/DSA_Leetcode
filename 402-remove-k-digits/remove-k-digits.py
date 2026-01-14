class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack=[]
        for i in range(len(num)):
            while stack and k>0 and stack[-1]>num[i]:
                stack.pop()
                k-=1
            stack.append(num[i])
        while stack and k>0:
            stack.pop()
            k-=1
        if not stack:
            return "0"
        
        res=""
        while stack:
            res+=stack.pop()
        res=res.rstrip('0')

        res=res[::-1]

        if not res:
            return "0"
        
        return res