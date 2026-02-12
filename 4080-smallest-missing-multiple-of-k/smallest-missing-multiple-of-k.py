class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        sett=set()
        for n in nums:
            sett.add(n)
        i=1
        while True:
            if i%k==0 and i not in sett:
                return i
            i+=1
        
        