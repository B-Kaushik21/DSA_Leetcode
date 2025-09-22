class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freqs={}
        for num in nums:
            if num not in freqs:
                freqs[num]=1
            else:
                freqs[num]+=1
        max_freq=max(freqs.values())
        count=0
        for num,freq in freqs.items():
            if freq==max_freq:
                count+=freq
        return count