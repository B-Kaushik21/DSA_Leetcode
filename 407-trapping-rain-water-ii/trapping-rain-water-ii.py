class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        
        m,n=len(heightMap),len(heightMap[0])
        if m<=2 or n<=2:
            return 0
        
        visited=[[False]*n for _ in range(m)]
        heap=[]

        for i in range(m):
            heapq.heappush(heap,(heightMap[i][0],i,0))
            heapq.heappush(heap,(heightMap[i][n-1],i,n-1))
            visited[i][0]=visited[i][n-1]=True
        
        for j in range(1,n-1):
            heapq.heappush(heap,(heightMap[0][j],0,j))
            heapq.heappush(heap,(heightMap[m-1][j],m-1,j))
            visited[0][j]=visited[m-1][j]=True
        
        res=0
        water_level=0
        dir=[(1,0),(-1,0),(0,1),(0,-1)]

        while heap:
            h,i,j=heapq.heappop(heap)
            water_level=max(water_level,h)

            for di,dj in dir:
                i0=i+di
                j0=j+dj
                if 0<= i0<m and 0<=j0<n and not visited[i0][j0]:
                    visited[i0][j0]=True
                    cur=heightMap[i0][j0]
                    if cur<water_level:
                        res+=water_level-cur
                    heapq.heappush(heap,(cur,i0,j0))
        return res