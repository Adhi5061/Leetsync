class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        def cosum(pos,curr,csum):
            if(csum==target):
                 if(curr[:] not in res):
                        res.append(curr[:])
                 return
            if(csum>target):
                return
            if(pos==len(candidates)):
                print(curr)
                return
            csum+=candidates[pos]
            curr.append(candidates[pos])
            cosum(pos,curr,csum)
            csum-=curr.pop()
            
            cosum(pos+1,curr,csum)
            
            # csum+=candidates[pos]
               
            # cosum(pos+1,curr,csum)
            # curr.pop()
            
        cosum(0,[],0)
        return res