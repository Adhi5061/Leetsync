# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=None
        while(head):
            n=head.next
            head.next=temp
            temp=head
            head=n
        head=temp
        summa=None
        reminder=0
        while(temp):
            val=temp.val*2
            node=ListNode(val%10+reminder)
            reminder=val//10
            node.next=summa
            summa=node
            temp=temp.next
        if(reminder!=0):
            node=ListNode(reminder)
            node.next=summa

        return node