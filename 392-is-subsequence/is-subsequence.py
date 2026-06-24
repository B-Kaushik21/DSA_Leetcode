class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s1 = Counter(s)
        t_iter = iter(t)  

        for ch in s:
            if ch in t_iter:  
                s1[ch] -= 1
                if s1[ch] == 0:
                    del s1[ch]

        return len(s1) == 0