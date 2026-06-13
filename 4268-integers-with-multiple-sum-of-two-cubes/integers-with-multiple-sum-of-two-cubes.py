class Solution:
    def findGoodIntegers(self, n: int) -> list[int]:
        map=defaultdict(int)
        res=[]
        limit=int(n**(1/3))
        for i in range(1,limit+1):
            i3=i*i*i
            for j in range(i,limit+1):
                s=i3+j*j*j
                if s>n:
                    break
                
                map[s]+=1
        for k,v in map.items():
            if v>=2:
                res.append(k)
        
        res.sort()
        return res