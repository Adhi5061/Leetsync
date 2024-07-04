# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head.next
        temp2=head
        cval=0
        while(temp):
            if(temp.val==0):
                temp.val=cval
                cval=0
                temp2.next=temp
                temp2=temp2.next
                temp=temp.next
            else:
                cval+=temp.val
                temp=temp.next
        return head.next
        # temp=head.next
        # prehead=head
        # csum=0
        # while(temp):
        #     if(temp.val==0):
        #         temp.val=csum
        #         csum=0
        #         prehead.next=temp
        #         prehead=temp
        #     else:
        #         csum+=temp.val
        #     temp=temp.next
        # return head.next