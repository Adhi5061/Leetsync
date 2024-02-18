# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        t1=headA
        t2=headB
        # d={}
        # while(t1 and t2):
        #     if(t1 in d):
        #         return t1
        #     d[t1]=1
        #     if(t2 in d):
        #         return t2
        #     d[t2]=1
        #     t1=t1.next
        #     t2=t2.next
        # while(t1):
        #     if(t1 in d):
        #         return t1
        #     d[t1]=1
        #     t1=t1.next
        # while(t2):
        #     if(t2 in d):
        #         return t2
        #     d[t2]=1
        #     t2=t2.next
        # return None
        c1=0
        c2=0
        while(t1):
            c1+=1
            t1=t1.next
        while(t2):
            c2+=1
            t2=t2.next
        if(c1<c2):
            while(c1<c2):
                headB=headB.next
                c2-=1
        else:
            while(c2<c1):
                headA=headA.next
                c1-=1
        while(headA and headB):
            if(headA==headB):
                return(headA)
            headA=headA.next
            headB=headB.next
        return None