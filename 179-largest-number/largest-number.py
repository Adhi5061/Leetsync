class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(n1,n2):
            if(n1+n2>n2+n1):
                return(-1)
            else:
                return(1)        
        for ind,num in enumerate(nums):
            nums[ind]=str(num)
        nums=sorted(nums,key=cmp_to_key(compare))
        return(str(int("".join(nums))))
        
            