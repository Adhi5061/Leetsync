class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def backtrack(i,j,pos,visited):
            
            if(pos==len(word)):
                return True
            if(i<0 or j<0 or i==len(board) or j==len(board[0]) or visited[i][j]==1):
                return False
            # print(i,j,pos,visited[i][j])
            if(board[i][j]==word[pos]):
                visited[i][j]=1
                ans=backtrack(i+1,j,pos+1,visited) or backtrack(i-1,j,pos+1,visited) or backtrack(i,j+1,pos+1,visited) or backtrack(i,j-1,pos+1,visited)
                visited[i][j]=0
                return ans
            return False

        for i in range(0,len(board)):
            for j in range(0,len(board[0])):
                visited=[[0] *len(board[0]) for k in range(0,len(board))]
                if(backtrack(i,j,0,visited)):
                    print(i,j)
                    return True
        return False           