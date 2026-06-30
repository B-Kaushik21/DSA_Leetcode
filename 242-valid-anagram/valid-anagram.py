class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        S=Counter(s)
        for char in t:
            if char in S:
                S[char]-=1
                if S[char]<0:
                    return False
            else:
                return False
        return all(count==0 for count in S.values()) 
        