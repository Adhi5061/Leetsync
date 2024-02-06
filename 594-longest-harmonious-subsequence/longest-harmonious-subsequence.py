from collections import Counter
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        counter=sorted(Counter(nums).items())
        prev=0
        l=0
        for ind,val in counter:
            if(prev==0):
                prev=val
                prei=ind
                continue
            elif(ind-prei==1):
                l=max(l,prev+val)
            prev=val
            prei=ind
        return l