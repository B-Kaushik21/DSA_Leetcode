class Solution:
    def longestBalanced(self, s: str) -> int:
        maxi=float('-inf')
        n=len(s)
        for i in range(n):
            freq=defaultdict(int)
            max_freq=0
            for j in range(i,n):
                freq[s[j]]+=1
                max_freq=max(max_freq,freq[s[j]])
                length=j-i+1
                distinct=len(freq)
                if distinct*max_freq==length:
                    maxi=max(maxi,length)
        return maxi