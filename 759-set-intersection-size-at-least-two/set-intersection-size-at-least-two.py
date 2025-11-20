class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:(x[1],-x[0]))
        b=intervals[0][1]
        a=b-1
        cnt=2
        for l,r in intervals[1:]:
            if a>=l:
                continue # already 2 points inside
            if l>b:
                # no points inside add 2
                cnt+=2
                a=r-1
                b=r
            else:
                # exactly 1 point inside add 1
                cnt+=1
                a=b
                b=r
        return cnt