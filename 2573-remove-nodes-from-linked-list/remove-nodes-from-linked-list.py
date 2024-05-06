# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        stack=[head.val]
        head=head.next
        while(head):
            while(len(stack)>0 and stack[-1]<head.val):
                stack.pop()
            stack.append(head.val)
            head=head.next
        dummy=ListNode(0)
        temp=dummy
        i=0
        while(i<len(stack)):
            node=ListNode(stack[i])
            temp.next=node
            temp=temp.next
            i+=1
        return dummy.next