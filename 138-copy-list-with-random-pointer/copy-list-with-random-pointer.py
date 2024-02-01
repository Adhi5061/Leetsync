"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        head1=head
        while head1:
            new=Node(head1.val)
            new.next=head1.next
            head1.next=new
            head1=head1.next.next
        curr=head
        while(curr):
            if(curr.random):
                curr.next.random=curr.random.next
            else:
                curr.next.random=None
            curr=curr.next.next
        curr=head
        head2=None
        if(head):
            head2=head.next
        while(curr):
            temp=curr.next
            if(curr.next):
                curr.next=curr.next.next
            else:
                curr.next=None
            curr=temp
        return head2
