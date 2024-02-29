"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        res=[]
        def flat(head):
            if(head==None):
                return
            if(head.child):
                nextn=head.next
                flat(head.child)
                head.next=head.child
                head.child.prev=head
                head.child=None
                while(head.next):
                    head=head.next
                head.next=nextn
                if(nextn):
                    nextn.prev=head
            else:
                flat(head.next)
        flat(head)
        return(head)
            