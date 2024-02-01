# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        fast=slow=pre=head
        while fast and fast.next:
            pre=slow
            slow=slow.next
            fast=fast.next.next
        if(fast):
            pre=slow
            slow=slow.next
        pre.next=None

        prev=None
        while(slow):
            nextn=slow.next
            slow.next=prev
            prev=slow
            slow=nextn
        head2=prev
        head1=head
        while(head2):
            t1=head1.next
            head1.next=head2
            t2=head2.next
            head2.next=t1
            head1=t1
            head2=t2