class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq=[-1]*256
        n=len(s)
        l,r=0,0
        maxlen=0
        
        while r<n:
            if freq[ord(s[r])]!=-1:
                l=max(freq[ord(s[r])]+1,l)
            maxlen=max(maxlen,r-l+1)
            freq[ord(s[r])]=r
            r+=1
        return maxlen

