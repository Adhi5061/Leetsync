# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if(root==None):
            return []
        res=[]
        q=[root]
        left=0
        while(q):
            temp=[]
            for i in range(len(q)):
                curr=q.pop(0)
                temp.append(curr.val)
                if(curr.left):
                    q.append(curr.left)
                if(curr.right):
                    q.append(curr.right)
            if(left==0):
                res.append(temp)
            else:
                res.append(temp[::-1])
            left=(left+1)%2
        return res