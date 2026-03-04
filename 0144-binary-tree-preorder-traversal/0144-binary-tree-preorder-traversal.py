class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        def inorder(root):
            if not root:
                return
            res.append(root.val)
            inorder(root.left)
            inorder(root.right)

            
        inorder(root)
        return res