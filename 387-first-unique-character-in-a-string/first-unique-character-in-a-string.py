class Solution:
    def firstUniqChar(self, s: str) -> int:
        repeat=[0]*26
        for i in range(len(s)):
            j=ord(s[i])-ord('a')
            repeat[j]+=1
        #print(repeat)

        for i in range(len(s)):
            j=ord(s[i])-ord('a')
            if repeat[j]==1:
                return i
        return -1