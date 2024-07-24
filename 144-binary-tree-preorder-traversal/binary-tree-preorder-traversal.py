# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        stack=[]
        res=[]
        if(root==None):
            return res
        stack.append(root)
        while(stack):
            node=stack.pop()
            res.append(node.val)
            if(node.right):
                stack.append(node.right)
            if(node.left):
                stack.append(node.left)
        return res
        
        # res=[]
        # def dfs(root):
        #     if(root==None):
        #         return 
        #     res.append(root.val)
        #     dfs(root.left)
        #     dfs(root.right)
        # dfs(root)
        # return res
        # st=[]
        # res=[]
        # temp=root
        # while(st or temp):
        #     while(temp):
        #         res.append(temp.val)
        #         st.append(temp)
        #         temp=temp.left
        #     temp=st.pop().right
        # return res
        # res=[]
        # def post(root):
        #     if(root==None):
        #         return
        #     res.append(root.val)
        #     post(root.left)
        #     post(root.right)
        # post(root)
        # return res

        