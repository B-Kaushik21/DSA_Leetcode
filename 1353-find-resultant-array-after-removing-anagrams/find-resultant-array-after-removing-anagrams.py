class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        
        def valid(s, t):
            S = Counter(s)
            for char in t:
                if char in S:
                    S[char] -= 1
                    if S[char] < 0:
                        return False
                else:
                    return False
            return all(count == 0 for count in S.values())
        
        res=[words[0]]

        for i in range(1,len(words)):
            if not valid(words[i],words[i-1]):
                res.append(words[i])
        return res