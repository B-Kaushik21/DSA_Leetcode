class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        count=Counter(num%value for num in nums)
        stop=0
        for i in range(value):
            if count[i]<count[stop]:
                stop=i
        return value*count[stop] + stop