class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        # Returns (depth, node)
        # depth = max depth of subtree
        # node = subtree root that contains all deepest nodes
        def dfs(node):
            if not node:
                return (0, None)
            
            left_depth, left_node = dfs(node.left)
            right_depth, right_node = dfs(node.right)
            
            if left_depth > right_depth:
                return (left_depth + 1, left_node)
            elif right_depth > left_depth:
                return (right_depth + 1, right_node)
            else:
                # same depth → current node is the LCA of deepest
                return (left_depth + 1, node)
        
        return dfs(root)[1]

