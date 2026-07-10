class Solution {

    List<Integer> ans = new ArrayList<>();

    public List<Integer> postorderTraversal(TreeNode root) {
        post(root);
        return ans;
    }

    private void post(TreeNode root) {

        if (root == null)
            return;

        post(root.left);
        post(root.right);

        ans.add(root.val);
    }
}