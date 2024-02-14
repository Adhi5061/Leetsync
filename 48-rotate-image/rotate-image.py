class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        for i in range(0,n//2):
            for j in range(i,len(matrix)-i-1):
                o=n-1-i
                t=n-1-j
                th=n-1-o
                matrix[i][j],matrix[j][o],matrix[o][t],matrix[t][th]=matrix[t][th],matrix[i][j],matrix[j][o],matrix[o][t]
    