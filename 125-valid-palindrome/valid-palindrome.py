class Solution:
    def isPalindrome(self, s: str) -> bool:
        ns=''
        for char in s:
            if char.isalnum():
                ns+=char.lower()
        l,r=0,len(ns)-1
        while l<r:
            if ns[l]==ns[r]:
                l+=1
                r-=1
            else:
                return False
        return True
    