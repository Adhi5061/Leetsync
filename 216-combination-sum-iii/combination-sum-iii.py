class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res=[]

        def comb(pos,curr,target):
            if(len(curr)==k):
                if(target==0):
                    res.append(curr[:])
                return
            for i in range(pos,10):
                if(i>target):
                    break
                target-=i
                curr.append(i)
                comb(i+1,curr,target)
                target+=curr.pop()
        comb(1,[],n)
        return res