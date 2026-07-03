class Solution {

    List<List<Integer>> ans = new ArrayList<>();

    public List<List<Integer>> subsets(int[] nums) {

        backtrack(0, nums, new ArrayList<>());

        return ans;
    }

    private void backtrack(int start, int[] nums, List<Integer> path) {

        ans.add(new ArrayList<>(path));

        for (int i = start; i < nums.length; i++) {

            path.add(nums[i]);

            backtrack(i + 1, nums, path);

            path.remove(path.size() - 1);
        }
    }
}