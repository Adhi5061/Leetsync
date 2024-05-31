class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        prefix=[0]
        curr=0
        for i in arr:
            curr=curr^i
            prefix.append(curr)
        print(prefix)
        res=0
        for i in range(0,len(prefix)):
            for j in range(i+2,len(prefix)):
                if(prefix[j]==prefix[i]):
                    # print(i,j)
                    res+=j-i-1
        # while(right<)        
        return res