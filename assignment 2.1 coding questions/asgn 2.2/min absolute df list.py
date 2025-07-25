# Minimum Absolute Difference in BST
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        mindiff=float('inf')
        prev_val=float('-inf')
        stack=[]
        while root or stack:
            if root:
                stack.append(root)
                root=root.left
            else:
                root=stack.pop()
                mindiff=min(mindiff,root.val-prev_val)
                prev_val=root.val
                root=root.right
        return mindiff
