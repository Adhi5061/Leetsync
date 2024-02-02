class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l=0
        r=len(matrix)-1
        print(r)
        while(l<=r):
            mid=(l+r)//2
            if(matrix[mid][0]<=target and matrix[mid][-1]>=target):
                left=0
                right=len(matrix[mid])-1
                while(left<=right):
                    cen=(left+right)//2
                    if(matrix[mid][cen]==target):
                        return True
                    elif(matrix[mid][cen]<target):
                        left=cen+1
                    else:
                        right=cen-1
                return False
            elif(matrix[mid][0]<target):
                l=mid+1
            else:
                r=mid-1
        return False
                    