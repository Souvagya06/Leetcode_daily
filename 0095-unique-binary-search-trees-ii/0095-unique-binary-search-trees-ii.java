class Solution {
    public List<TreeNode> generateTrees(int n) {
        if (n == 0) return new ArrayList<>();
        return build(1, n);
    }

    private List<TreeNode> build(int start, int end) {
        List<TreeNode> res = new ArrayList<>();

        if (start > end) {
            res.add(null);
            return res;
        }

        for (int root = start; root <= end; root++) {
            List<TreeNode> left = build(start, root - 1);
            List<TreeNode> right = build(root + 1, end);

            for (TreeNode l : left) {
                for (TreeNode r : right) {
                    TreeNode node = new TreeNode(root);
                    node.left = l;
                    node.right = r;
                    res.add(node);
                }
            }
        }

        return res;
    }
}