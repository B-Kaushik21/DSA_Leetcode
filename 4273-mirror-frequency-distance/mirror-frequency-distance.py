class Solution:
    def mirrorFrequency(self, s: str) -> int:
        freq = Counter(s)
        res = 0
        seen = set()  # O(1) Lookups instead of string scanning

        for c in s:
            # 1. Compute mirror character using ASCII math
            if c.isalpha():
                m = chr(219 - ord(c))  # ord('a') + ord('z') = 97 + 122 = 219
            else:
                m = chr(105 - ord(c))  # ord('0') + ord('9') = 48 + 57 = 105

            # 2. Fast O(1) checking using the hash set
            if (c not in seen) and (m not in seen):
                res += abs(freq[c] - freq[m])
                seen.add(c)
                seen.add(m)
                
        return res
