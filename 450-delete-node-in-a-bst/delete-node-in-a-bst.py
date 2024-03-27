# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if(root==None):
            return root
        if(root.val==key):
            if(root.left and root.right):
                prev=root
                temp=root.right
                while(temp.left):
                    prev=temp
                    temp=temp.left
                if(prev==root):
                    root.val=temp.val
                    root.right=temp.right
                    return root
                prev.left=temp.right
                root.val=temp.val
                return root
            elif(root.left):
                return root.left
            else:
                return root.right
        if(root.val>key):
            root.left=self.deleteNode(root.left,key)
        else:
            root.right=self.deleteNode(root.right,key)
        return root