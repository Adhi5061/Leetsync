class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        snum=set(nums)
        count=0
        for i in snum:
            if(i-1 in snum):
                continue
            temp=1
            while(1):
                i+=1
                if(i in snum):
                    temp+=1
                else:
                    break
            if(temp>count):
                count=temp
        return count