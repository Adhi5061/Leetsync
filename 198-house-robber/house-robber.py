class Solution:
    def rob(self, nums: List[int]) -> int:
        if(len(nums)==1):
            return nums[0]
        table=[0]*len(nums)
        table[0]=nums[0]
        table[1]=nums[1]
        for i in range(0,len(nums)):
            for j in range(i+2,len(nums)):
                table[j]=max(table[j],table[i]+nums[j])
            # print(table)
        return max(table)
        
        
        # memo={}
        # def rob(arr,pos):
        #     if(len(arr)<=pos):
        #         memo[pos]=0
        #         return 0
        #     if(len(arr)-pos==1):
        #         memo[pos]=arr[pos]
        #         return arr[pos]
        #     if(pos in memo):
        #         return memo[pos]
        #     memo[pos]= max(arr[pos]+rob(arr,pos+2),arr[pos+1]+rob(arr,pos+3))
        #     return memo[pos]
        # return rob(nums,0)