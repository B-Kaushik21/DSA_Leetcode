class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        count=0
        m=len(bank)
        devices=[row.count('1') for row in bank]
        for r1 in range(m):
            for r2 in range(r1+1,m):
                empty=all(devices[k]==0 for k in range(r1+1,r2))
                if empty:
                    count+=devices[r1]*devices[r2]

        return count