class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        low,up={},{}
        for i,c in enumerate(word):
            if c.islower():
                low[c]=i
            else:
                if c not in up:
                    up[c]=i
        ans = 0
        for i in range(26):
            c = chr(ord('a') + i)
            upper_c = chr(ord('A') + i)

            if c in low:
                if upper_c in up:
                    if low[c] < up[upper_c]:
                        ans += 1

        return ans