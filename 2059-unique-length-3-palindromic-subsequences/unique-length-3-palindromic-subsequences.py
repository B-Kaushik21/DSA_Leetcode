class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        count=0
        for char in string.ascii_lowercase:
            i,j = s.find(char),s.rfind(char)
            if i>-1:
                count+=len(set(s[i+1:j]))
        return count