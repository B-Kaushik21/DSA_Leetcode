class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        res=''
        for w in words:
            ans=0
            for i in range(len(w)):
                ans+=(weights[ord(w[i])-ord('a')])
            res+=chr(25-(ans%26)+97)
        return res