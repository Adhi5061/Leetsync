# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        from collections import deque
        if(root==None):
            return 0
        q=deque()
        q.append(root)
        level=0
        while(q):
            l=len(q)
            level+=1
            for i in range(l):
                node=q.popleft()
                if(node.left):
                    q.append(node.left)
                if(node.right):
                    q.append(node.right)
        return level
        # def depth(root):
        #     if(root==None):
        #         return 0
        #     return 1+max(depth(root.left),depth(root.right))
        # return depth(root)