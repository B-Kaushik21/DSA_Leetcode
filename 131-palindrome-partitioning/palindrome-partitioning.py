class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res=[]
        temp=[]
        def backtrack(index):
            #base condition
            if index==len(s):
                res.append(temp[:])
                return
            for i in range(index,len(s)):
                if isPalindrome(s,index,i):
                    temp.append(s[index:i+1])
                    backtrack(i+1)
                    temp.pop()
        def isPalindrome(s,start,end):
            while start<=end:
                if s[start]!=s[end]:
                    return False
                start+=1
                end-=1
            return True
        backtrack(0)
        return res