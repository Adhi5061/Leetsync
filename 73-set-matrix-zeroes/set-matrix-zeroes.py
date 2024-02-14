class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero=set()
        for rowi in range(0,len(matrix)):
            zer=False
            for valuei in range(0,len(matrix[rowi])):
                if(matrix[rowi][valuei]==0):
                    zero.add(valuei)
                    zer=True
            if(zer):
                matrix[rowi]=[0]*len(matrix[rowi])
        print(zero)      
        
        for row in matrix:
            for coli in range(0,len(row)):
                if(coli in zero):
                    row[coli]=0