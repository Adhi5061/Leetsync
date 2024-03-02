# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fin=fake=ListNode(-100)
        fake.next=head
        temp=head
        while(temp and temp.next):
            if(temp.val==temp.next.val):
                val=temp.val
                temp2=temp.next
                while(temp2 and temp2.val==val):
                    temp2=temp2.next
                if(temp2):
                    temp.val=temp2.val
                    temp.next=temp2.next
                else:
                    fake.next=None
                    break
            else:
                temp=temp.next
                fake=fake.next
        return(fin.next)
        