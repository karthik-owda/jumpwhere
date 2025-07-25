# Average of Levels in Binary Tree
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue=deque([root])
        result=[]

        while queue:
            level=[]
            for i in range(len(queue)):
                node=queue.popleft()
                level.append(node.val)
                print(level)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(sum(level)/len(level))
        return result
