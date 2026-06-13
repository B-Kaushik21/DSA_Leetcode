class Solution:
    def mirrorFrequency(self, s: str) -> int:
        freq=Counter(s)
        #print(freq)
        res=0
        seen=''

        set1={'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}

        set2={1: 'z', 2: 'y', 3: 'x', 4: 'w', 5: 'v', 6: 'u', 7: 't', 8: 's', 9: 'r', 10: 'q', 11: 'p', 12: 'o', 13: 'n', 14: 'm', 15: 'l', 16: 'k', 17: 'j', 18: 'i', 19: 'h', 20: 'g', 21: 'f', 22: 'e', 23: 'd', 24: 'c', 25: 'b', 26: 'a'}

        digit={'0':'9','1':'8','2':'7','3':'6','4':'5','5':'4','6':'3','7':'2','8':'1','9':'0'}

        for c in s:
            if c.isalpha():
                m=set2[set1[c]]
                print(m)
            elif c.isdigit():
                m=digit[c]
            if (c not in seen) and (m not in seen):
                res+=abs(freq[c]-freq[m])
                seen+=c+m
                
        return res
