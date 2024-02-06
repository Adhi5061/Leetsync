class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        left=0
        right=min(k,len(nums)-1)
        chack=min(k,len(nums)-1)
        l=len(nums)
        window=set(nums[left:right])
        while(right<l):    
            window.add(nums[right])
            if(len(window)<=chack):
                return True
            window.remove(nums[right-k])
            right+=1
        return False