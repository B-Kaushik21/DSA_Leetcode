class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows=len(board)
        cols=len(board[0])

        def dfs(i,j,ind):
            #if all chars matched
            if ind==len(word):
                return True
            #boundary and char check
            if i<0 or j<0 or i>=rows or j>=cols or board[i][j]!=word[ind]:
                return False
            
            #store char and mark visited
            temp=board[i][j]
            board[i][j]='#'

            #exploring all four directions 
            found= (dfs(i+1,j,ind+1) or 
                    dfs(i-1,j,ind+1) or 
                    dfs(i,j-1,ind+1) or 
                    dfs(i,j+1,ind+1))
        
            #restore temp
            board[i][j]=temp
            return found

        for i in range(rows):
            for j in range(cols):
                if dfs(i,j,0):
                    return True
        return False