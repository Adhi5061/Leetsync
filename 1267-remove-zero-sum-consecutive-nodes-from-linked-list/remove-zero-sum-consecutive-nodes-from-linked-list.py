# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        temp=head
        arr=[]
        while(temp):
            arr.append(temp.val)
            temp=temp.next
        positions=[]
        for i in range(0,len(arr)):
            if(i in positions):
                continue
            for j in range(i,len(arr)):
                if(i in positions or j in positions):
                    continue
                if(sum(arr[i:j+1])==0):
                    positions.extend(list(range(i,j+1)))
        positions.sort(reverse=True)
        for i in positions:
            arr.pop(i)
        head=None
        if(len(arr)>0):
            head=ListNode(arr[0])
        temp=head
        for i in range(1,len(arr)):
            node=ListNode(arr[i])
            temp.next=node
            temp=temp.next
        return head