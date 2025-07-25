# Same Tree
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack=[(p,q)]
        while stack:
            node1,node2=stack.pop()
            if not node1 and not node2:
                continue
            elif None in [node1,node2] or node1.val!= node2.val:
                return False
            stack.append((node1.right,node2.right))
            stack.append((node1.left,node2.left))
        return True
