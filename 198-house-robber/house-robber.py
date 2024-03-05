class Solution:
    def rob(self, nums: List[int]) -> int:
        memo={}
        def rob(arr,pos):
            if(len(arr)<=pos):
                memo[pos]=0
                return 0
            if(len(arr)-pos==1):
                memo[pos]=arr[pos]
                return arr[pos]
            if(pos in memo):
                return memo[pos]
            memo[pos]= max(arr[pos]+rob(arr,pos+2),arr[pos+1]+rob(arr,pos+3))
            return memo[pos]
        return rob(nums,0)