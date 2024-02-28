class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res=[]
        def sub(curr,pos):
            if(len(curr)==k):
                res.append(curr[:])
                return
            for i in range(pos,n+1):
                curr.append(i)
                sub(curr,i+1)
                curr.pop()
        sub([],1)
        return res