# Search in a Binary Search Tree
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        while root:
            if root.val==val:
                return root
            elif root.val<val:
                root=root.right
            else:
                root=root.left
        return None
