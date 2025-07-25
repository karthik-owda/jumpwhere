# Balance a Binary Search Tree
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def inorder_traversal(node: Optional[TreeNode]) -> List[int]:
            if not node:
                return []
            return inorder_traversal(node.left) + [node.val] + inorder_traversal(node.right)

        def sorted_list_to_bst(start: int, end: int) -> Optional[TreeNode]:
            if start > end:
                return None
            mid = (start + end) // 2
            root = TreeNode(values[mid])  
            root.left = sorted_list_to_bst(start, mid - 1) 
            root.right = sorted_list_to_bst(mid + 1, end)  
            return root

        values = inorder_traversal(root)

        return sorted_list_to_bst(0, len(values) - 1)
