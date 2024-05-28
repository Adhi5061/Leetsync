class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        count=0
        i=0
        j=1
        while(j<len(arr)):
            if(arr[i]>arr[j]):
                count+=1
            else:
                i=j
                count=1
            if(count==k):
                return arr[i]
            j+=1
        return arr[i]