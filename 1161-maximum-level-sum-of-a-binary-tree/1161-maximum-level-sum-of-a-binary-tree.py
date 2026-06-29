from collections import deque

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        queue = deque([root])
        max_sum = float('-inf')
        best_level = 1
        level = 1
        
        while queue:
            level_size = len(queue)
            current_sum = 0
            
            for _ in range(level_size):
                node = queue.popleft()
                current_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            if current_sum > max_sum:
                max_sum = current_sum
                best_level = level
            
            level += 1
        
        return best_level
