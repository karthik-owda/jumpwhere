# Minimum Depth of Binary Tree
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue=deque([(root,1)])
        while queue:
            node,level=queue.popleft()
            if not node.left and not node.right:
                return level
            if node.left:
                queue.append((node.left,level+1))
            if node.right:
                queue.append((node.right,level+1))
        return 0
