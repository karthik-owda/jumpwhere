# Invert Binary Tree
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack=[root]
        while stack:
            curr=stack.pop()
            if curr:
                curr.left,curr.right=curr.right,curr.left
                stack.extend([curr.right,curr.left])
        return root
