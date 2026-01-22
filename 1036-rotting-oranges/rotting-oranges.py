class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        if not grid:
            return 0
        q=deque()
        total,count=0,0
        for i in range(n):
            for j in range(m):
                if grid[i][j]!=0:
                    total+=1
                if grid[i][j]==2:
                    q.append((i,j))
        dir=[(0,1),(0,-1),(1,0),(-1,0)]
        time=0
        while q:
            k=len(q)
            count+=k
            for _ in range(k):
                x,y=q.popleft()
                for dx,dy in dir:
                    nx=x+dx
                    ny=y+dy
                    if nx<0 or ny<0 or nx>=n or ny>=m or grid[nx][ny]!=1:
                        continue
                    
                    grid[nx][ny]=2

                    q.append((nx,ny))
            if q:
                time+=1
        return time if count==total else -1
