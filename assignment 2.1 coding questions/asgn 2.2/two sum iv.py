# Two Sum IV - Input is a BST
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        queue=deque([root])
        num=set()
        while queue:
            node=queue.popleft()
            if (k-node.val) in num:
                return True
            else:
                num.add(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return False
