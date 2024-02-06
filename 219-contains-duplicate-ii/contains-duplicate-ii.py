class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        pos={}
        for ind,val in enumerate(nums):
            if(val in pos):
                if(ind-pos[val][-1]<=k):
                    return True
                pos[val].append(ind)
            else:
                pos[val]=[ind]
        return False