class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        def count(k):
            if(k<0):
                return 0
            res=0
            l=0
            r=0
            csum=0
            while(r<len(nums)):
                csum+=nums[r]
                while(csum>k):
                    csum-=nums[l]
                    l+=1
                res+=r-l+1
                r+=1
            return res

        return(count(goal)-count(goal-1))
        # count=0
        # l=0
        # r=0
        # csum=0
        # rc=lc=0
        # while(r<len(nums)):
        #     print(l,r)
        #     if(csum<goal):
        #         csum+=nums[r]
        #         r+=1
        #     if(csum==goal):
        #         print("Goal reached")
        #         if(nums[r]==0):
        #             rc+=1
        #             r+=1
        #         else:
        #             count+=(lc+rc+lc*rc+1)
        #             while(nums[l]==0):
        #                 l+=1
        #             csum-=nums[l]
        #             l+=1
        #             r+=1
        #     else:
        #         csum-=nums[l]
        #         l+=1
        # return 0

        # count=0
        # d={}
        # flag=False
        # start=-1
        # end=-1
        # for i  in range(0,len(nums)):
        #     if(nums[i]==0 and not flag):
        #         start=i
        #         flag=True
        #     if(nums[i]==1 and flag):
        #         end=i-1
        #         d[start]=end
        #         flag=False
        # if(flag):
        #     d[start]=i
        # i=0
        
        # while(i<len(nums)):
        #     print("Outside",i,count)
        #     t=0
        #     while(i<len(nums) and i>0 and nums[i]==0 and nums[i-1]==0 and goal!=0):
        #         #print("Hello")
        #         print("Inside i",i)
        #         count+=temp
        #         h=0
        #         i+=1
        #     temp=0
        #     j=i
        #     while(j<len(nums)):
        #         t+=nums[j]
        #         if(nums[j]==0 and t!=goal):
        #             j=d[j]+1
        #             continue
        #         if(t==goal):
        #             #print("t==goal")
        #             j+=1
        #             count+=1
        #             temp+=1
        #             continue
        #         if(t>goal):
        #             j+=1
        #             break
        #         j+=1
        #     h=1
            
        #     if(h):
        #         i+=1
        # return count