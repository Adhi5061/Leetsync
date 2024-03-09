# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        # res=[]
        # def post(root):
        #     if(root==None):
        #         return
        #     res.append(root.val)
        #     post(root.left)
        #     post(root.right)
        # post(root)
        # return res

        st=[]
        res=[]
        temp=root
        while(st or temp):
            while(temp):
                res.append(temp.val)
                st.append(temp)
                temp=temp.left
            temp=st.pop().right
        return res