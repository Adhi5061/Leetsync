class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        x=[0,0,1,-1]
        y=[1,-1,0,0]
        def dfs(i,j):
            if(i<0 or i>=len(board) or j<0 or j>=len(board[0])):
                return
            if(board[i][j]=='O'):
                board[i][j]='M'
                for ind in range(4):
                    dfs(i+x[ind],j+y[ind])

        for i in range(0,len(board)):
            if(board[i][0]=="O"):
                dfs(i,0)
            if(board[i][len(board[0])-1]=="O"):
                dfs(i,len(board[0])-1)
        for j in range(0,len(board[0])):
            if(board[0][j]=="O"):
                dfs(0,j)
            if(board[len(board)-1][j]=="O"):
                dfs(len(board)-1,j)
        
        for i in range(0,len(board)):
            for j in range(0,len(board[0])):
                if(board[i][j]=="M"):
                    board[i][j]="O"
                elif(board[i][j]=="O"):
                    board[i][j]="X"
        