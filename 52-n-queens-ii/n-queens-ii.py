class Solution:
    def totalNQueens(self, n: int) -> int:
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
                return 1
            ans=0
            for i in range(0,n):
                if(check(row,i,-1,1,mat) and check(row,i,-1,-1,mat) and check(row,i,-1,0,mat)):
                    mat[row][i]="Q"
                    ans+=queen(row+1)
                    mat[row][i]="."
            return ans
        return queen(0)
        return res

