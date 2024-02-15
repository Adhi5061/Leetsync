class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        i=0
        j=0
        l=t=0
        b=len(matrix)-1
        r=len(matrix[0])-1
        res=[]
        while(l<=r and t<=b):
            i=l
            j=t
            while(i<=r):
                res.append(matrix[j][i])
                i+=1
            i-=1
            t+=1
            j=t
            print("Value of i,j",i,j)
            while(j<=b):
                res.append(matrix[j][i])
                j+=1
            j-=1
            r-=1
            i=r
            while(i>=l and t<=b):
                res.append(matrix[j][i])
                i-=1
            i+=1
            b-=1
            j=b
            while(j>=t and l<=r):
                res.append(matrix[j][i])
                j-=1
            j+=1
            l+=1
        return res