class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less,more,count=[],[],0
        for num in nums:
            if num==pivot:
                count+=1
        for num in nums:
            if num<pivot:
                less.append(num)
            elif num>pivot:
                more.append(num)
        
        return less+ [pivot]* count + more
