# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        temp=head
        prev=None
        while(left>1):
            prev=temp
            temp=temp.next
            left-=1
            right-=1
        fb=temp
        pre=None
        while(right>0):
            ne=temp.next
            temp.next=pre
            pre=temp
            temp=ne
            right-=1
        if(prev):
            prev.next=pre
            fb.next=temp
            return head
        fb.next=temp
        return pre
        
        