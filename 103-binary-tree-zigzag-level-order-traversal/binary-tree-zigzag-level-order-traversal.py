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
                if(left==0):
                    temp.append(curr.val)
                else:
                    temp.insert(0,curr.val)
                if(curr.left):
                    q.append(curr.left)
                if(curr.right):
                    q.append(curr.right)
               
            left=(left+1)%2
            res.append(temp)
        return res