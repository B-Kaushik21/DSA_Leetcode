class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        for num in nums:
            if num not in freq:
                freq[num]=1
            else:
                freq[num]+=1
        freq=dict(sorted(freq.items(),key=lambda x:x[1],reverse=True))
        res=list(freq.keys())[:k]
        return res