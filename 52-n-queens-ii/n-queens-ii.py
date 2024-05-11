class Solution:
    def totalNQueens(self, n: int) -> int:
        import copy
        import numpy as np
        def check(row,col,i,j,mat):
            i=row
            j=col
            while(i>=0 and j>=0):
                if(mat[i][j]=="Q"):
                    return 0
                i-=1
                j-=1
            i=row
            j=col
            while(i>=0 and j<n):
                if(mat[i][j]=="Q"):
                    return 0
                i-=1
                j+=1
            i=row
            while(i>=0):
                if(mat[i][col]=="Q"):
                    return 0
                i-=1
            return 1
        
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

