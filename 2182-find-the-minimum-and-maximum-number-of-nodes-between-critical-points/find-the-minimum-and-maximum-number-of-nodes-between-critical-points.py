# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        left=100000
        right=0
        prev=head
        temp=head.next
        cval=1
        minv=100000
        prevval=-100000
        cp=0
        while(temp and temp.next):
            if(temp.val>temp.next.val and temp.val>prev.val):
                left=min(left,cval)
                right=max(right,cval)
                minv=min(minv,cval-prevval)
                prevval=cval
                cp+=1
            if(temp.val<temp.next.val and temp.val<prev.val):
                left=min(left,cval)
                right=max(right,cval)
                minv=min(minv,cval-prevval)
                prevval=cval
                cp+=1
            prev=temp
            temp=temp.next
            cval+=1
        if(left==100000 or right==0 or cp<2):
            return [-1,-1]
        else:
            return ([minv,right-left])