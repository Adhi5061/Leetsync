# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        q=deque()
        q.append(root)
        if(not root):
            return []
        while(q):
            ans=0
            for i in range(len(q)):
                node=q.popleft()
                ans=node.val
                if(node.left):
                    q.append(node.left)
                if(node.right):
                    q.append(node.right)
            res.append(ans)
        return res