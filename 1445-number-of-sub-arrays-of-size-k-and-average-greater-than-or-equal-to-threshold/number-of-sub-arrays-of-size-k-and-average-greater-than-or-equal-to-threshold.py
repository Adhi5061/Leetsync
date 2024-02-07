class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count=0
        csum=sum(arr[:k])
        left=-1
        right=k-1
        while(1):
            print(csum,left,right,count)
            if(csum/k>=threshold):
                count+=1
            left+=1
            right+=1
            if(right>=len(arr)):
                break
            csum-=arr[left]
            csum+=arr[right]
        return count