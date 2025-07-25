# Delete Node in a BST
class Solution:
     def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        parent = None
        current = root

        while current and current.val != key:
            parent = current
            if key < current.val:
                current = current.left
            else:
                current = current.right

        if not current:
            return root

        if not current.left and not current.right:
            if not parent:
                return None 
            if parent.left == current:
                parent.left = None
            else:
                parent.right = None

        elif not current.left or not current.right:
            child = current.left if current.left else current.right
            if not parent:
                return child  
            if parent.left == current:
                parent.left = child
            else:
                parent.right = child

        else:
            successor_parent = current
            successor = current.right
            while successor.left:
                successor_parent = successor
                successor = successor.left
            
            current.val = successor.val
            if successor_parent.left == successor:
                successor_parent.left = successor.right
            else:
                successor_parent.right = successor.right
        
        return root
