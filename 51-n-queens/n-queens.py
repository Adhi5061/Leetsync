class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        import copy
        import numpy as np
        def check(row,col,i,j,mat):
            if(row<0 or col<0 or row==n or col==n):
                return True
            if(mat[row][col]=="Q"):
                return False
            return check(row+i,col+j,i,j,mat)
        
        res=[]
        mat=[["."]*n for i in range(n)]
        def queen(row):
            if(row==n):
                res.append([])
                for i in mat:
                    t="".join(i)
                    # print(t)
                    res[-1].append(t)
                # res.append(mat)
                return 
            for i in range(0,n):
                if(check(row,i,-1,1,mat) and check(row,i,-1,-1,mat) and check(row,i,-1,0,mat)):
                    mat[row][i]="Q"
                    queen(row+1)
                    mat[row][i]="."
        queen(0)
        return res

