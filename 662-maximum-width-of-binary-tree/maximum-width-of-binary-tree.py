# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxw=0
        q=deque()
        no=1
        q.append((root,1))
        while(q):
            l=len(q)
            # for i in range(0,l):
            #     print(q[i][1],end=" ")
            # # print()
            maxw=max(maxw,q[-1][1]-q[0][1]+1)
            for i in range(0,l):
                node,no=q.popleft()
                if(node.left):
                    q.append((node.left,2*no))
                if(node.right):
                    q.append((node.right,2*no+1))
            # print(maxw)
        return maxw