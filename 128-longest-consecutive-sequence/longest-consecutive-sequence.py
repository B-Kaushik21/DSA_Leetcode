class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sett=set(nums)
        longest=0

        for num in sett:
            if num-1 not in sett:#check sequence 
                curr=num
                length=1

                while curr+1 in sett:
                    curr+=1
                    length+=1
                longest=max(longest,length)
        return longest