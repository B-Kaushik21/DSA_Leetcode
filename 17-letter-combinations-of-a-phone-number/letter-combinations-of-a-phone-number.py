class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        store= ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        ans=[]
        if not digits:
            return ans
        def dfs(digits,ans,index,current):
            #base condition
            if index==len(digits):
                ans.append(current)
                return 
            #characters corresponding to curr digit
            s=store[int(digits[index])]
            #loop through corresponding characters
            for char in s:
                #call next index recursively
                dfs(digits,ans,index+1,current+char)
        dfs(digits,ans,0,"")
        return ans