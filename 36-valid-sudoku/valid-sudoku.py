class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        def check(row,col,no,mat):
            for i in range(0,9):
                if(mat[row][i]==no):
                    return 0
                if(mat[i][col]==no):
                    return 0
            sr=row-row%3
            sc=col-col%3
            # if(row==1 and col==2):
            #     print(mat,no,sr,sc)
            for i in range(sr,sr+3):
                for j in range(sc,sc+3):
                    if(mat[i][j]==no):
                        # print("HI")
                        return 0
            # print(sr,sc,row,col,no)
            return 1

        for i in range(0,9):
            for j in range(0,9):
                if(board[i][j]=="."):
                    continue
                t=board[i][j]
                board[i][j]="."
                if(check(i,j,t,board)==0):
                    print(i,j)
                    return False
                board[i][j]=t
        return True