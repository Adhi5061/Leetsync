# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(not head or not head.next):
            return head
        oddh=ot=head
        evenh=et=head.next
        curr=head
        while(curr and curr.next):
            temp=curr.next
            curr.next=temp.next
            curr=temp
        while(oddh.next):
            oddh=oddh.next
        oddh.next=evenh
        return head