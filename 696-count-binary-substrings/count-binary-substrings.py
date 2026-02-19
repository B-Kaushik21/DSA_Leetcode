class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        cur,pre,res=1,0,0
        for i in range(1,len(s)):
            if s[i]==s[i-1]:
                cur+=1
            else:
                res+=min(cur,pre)
                pre=cur
                cur=1
        return res+min(cur,pre)