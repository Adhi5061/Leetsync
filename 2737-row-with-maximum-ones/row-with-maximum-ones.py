class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        r=0
        mc=c=0
        for index,row in enumerate(mat):
            c=row.count(1)
            if(c>mc):
                mc=c
                r=index
        return([r,mc])

        