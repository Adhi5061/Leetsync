# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        res=[]
        
        def dfs(root,csum,temp):
            if(root==None):
                return 
            csum+=root.val
            temp.append(root.val)
            if(root.left==None and root.right==None):
                if(csum==targetSum):
                    res.append(temp[:])
                temp.pop()
                return
            dfs(root.left,csum,temp)
            dfs(root.right,csum,temp)
            temp.pop()
        dfs(root,0,[])
        return res