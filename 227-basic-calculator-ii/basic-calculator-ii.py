class Solution:
    def calculate(self, s: str) -> int:
        n=len(s)
        if not s:
            return 0
        stack=[]
        op='+'
        res=0
        for i,ch in enumerate(s):
            if ch.isdigit():
                res=res*10+int(ch)
            if ch in '+-*/' or i==n-1:
                if op=='+':
                    stack.append(res)
                elif op=='-':
                    stack.append(-res)
                elif op=='*':
                    prev=stack.pop()
                    stack.append(prev*res)
                elif op=='/':
                    prev=stack.pop()
                    stack.append(int(prev/res))
                op=ch
                res=0
        return sum(stack)