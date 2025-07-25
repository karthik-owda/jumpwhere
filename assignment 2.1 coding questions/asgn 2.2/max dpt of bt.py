# Maximum Depth of Binary Tree
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue=deque([(root,1)])
        while queue:
            node,level=queue.popleft()
            if node.right:
                queue.append((node.right,level+1))
            if node.left:
                queue.append((node.left,level+1))
        return level
