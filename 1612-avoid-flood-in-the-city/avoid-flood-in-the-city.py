class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        n=len(rains)
        ans=[1]*n
        last_rain_day={}
        dry_days=SortedList()
        for i, lake in enumerate(rains):
            if lake==0:
                dry_days.add(i)
            else:
                if lake in last_rain_day:
                    prev=last_rain_day[lake]
                    index=dry_days.bisect_right(prev)
                    if index==len(dry_days):
                        return []
                    dry_day=dry_days[index]
                    ans[dry_day]=lake
                    dry_days.remove(dry_day)
                last_rain_day[lake]=i
                ans[i]=-1
        return ans