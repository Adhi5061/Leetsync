class Solution:
    def minPartitions(self, n: str) -> int:
        res=0
        for i in n:
            if(int(i)>res):
                res=int(i)
        return res
        