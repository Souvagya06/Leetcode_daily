class Solution {
    public boolean isValidBST(TreeNode root) {
        return dfs(root, Long.MIN_VALUE, Long.MAX_VALUE);
    }

    private boolean dfs(TreeNode node, long low, long high) {
        if (node == null)
            return true;

        if (node.val <= low || node.val >= high)
            return false;

        return dfs(node.left, low, node.val)
                && dfs(node.right, node.val, high);
    }
}