class Solution {

    List<List<Integer>> ans = new ArrayList<>();

    public List<List<Integer>> pathSum(TreeNode root, int targetSum) {
        dfs(root, targetSum, new ArrayList<>());
        return ans;
    }

    private void dfs(TreeNode node, int sum, List<Integer> path) {
        if (node == null) return;

        path.add(node.val);

        if (node.left == null && node.right == null && sum == node.val) {
            ans.add(new ArrayList<>(path));
        } else {
            dfs(node.left, sum - node.val, path);
            dfs(node.right, sum - node.val, path);
        }

        path.remove(path.size() - 1);
    }
}