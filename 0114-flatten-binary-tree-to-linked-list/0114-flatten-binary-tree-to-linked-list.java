class Solution {

    TreeNode prev;

    public void flatten(TreeNode root) {
        prev = null;
        helper(root);
    }

    private void helper(TreeNode root) {
        if (root == null) return;

        helper(root.right);
        helper(root.left);

        root.right = prev;
        root.left = null;
        prev = root;
    }
}