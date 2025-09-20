class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort()
        n=len(intervals)
        res=[]
        i=0
        while i<n:
            start,end=intervals[i]
            while i+1<n and end>=intervals[i+1][0]:
                end=max(end,intervals[i+1][1])
                i+=1
            res.append([start,end])
            i+=1
        return res