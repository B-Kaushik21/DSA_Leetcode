class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n,l,r,maxlen=len(fruits),0,0,0
        freq={}
        while r<n:
            freq[fruits[r]]=freq.get(fruits[r],0)+1
            while len(freq)>2:
                freq[fruits[l]]-=1
                if freq[fruits[l]]==0:
                    del freq[fruits[l]]
                l+=1
            maxlen=max(maxlen,r-l+1)
            r+=1
        return maxlen