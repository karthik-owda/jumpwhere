# Lowest Common Ancestor of a Binary Search Tree
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        small=min(p.val,q.val)
        large=max(p.val,q.val)
        while root:
            if root.val>large:
                root=root.left
            elif root.val<small:
                root=root.right
            else:
                return root
        return None
