# Diameter of Binary Tree
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter=0
        def depth(root):
            if not root:
                return 0
            left_depth=depth(root.left)
            right_depth=depth(root.right)

            self.diameter=max(self.diameter,left_depth+right_depth)
            return 1+max(left_depth,right_depth)
        depth(root)
        return self.diameter
