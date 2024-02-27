class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        candidates.sort()
        def cosum(pos,curr,csum):
            if(csum==target):
                res.append(curr[:])
                return
            if(csum>target):
                return
            for i in range(pos,len(candidates)):
                if(candidates[i]>target-csum):
                    break
                if(i>pos and candidates[i]==candidates[i-1]):
                    continue
                curr.append(candidates[i])
                csum+=candidates[i]
                cosum(i+1,curr,csum)
                csum-=curr.pop()      
        cosum(0,[],0)
        return res