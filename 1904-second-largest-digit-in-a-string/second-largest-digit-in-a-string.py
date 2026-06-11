class Solution:
    def secondHighest(self, s: str) -> int:
        nums=set()
        for ch in s:
            if ch.isdigit():
                nums.add(int(ch))
        print(nums)
        if len(nums)<2:
            return -1
        nums=list(nums)
        first=second=float('-inf')
        n=len(nums)
        for i in range(n):
            if nums[i]>first:
                second=first
                first=nums[i]

            elif nums[i]<first and nums[i]>second:
                second=nums[i]
        return second