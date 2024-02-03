# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def merges(head):
            if(head==None or head.next==None):
                return head
            slow=head
            fast=head.next
            while(fast and fast.next):
                slow=slow.next
                fast=fast.next.next
            temp=slow.next
            slow.next=None
            left=merges(head)
            right=merges(temp)
            return merge(left,right)
        
        def merge(h1,h2):
            head=ListNode(0)
            header=head
            while(h1 and h2):
                if(h1.val<=h2.val):
                    head.next=h1
                    h1=h1.next
                else:
                    head.next=h2
                    h2=h2.next
                head=head.next
            if(h1):
                head.next=h1
            else:
                head.next=h2
            return header.next
        return(merges(head))