import java.util.*;

class Solution {

    public List<List<Integer>> combinationSum2(int[] candidates, int target) {

        List<List<Integer>> ans = new ArrayList<>();
        Arrays.sort(candidates);

        backtrack(candidates, target, 0, new ArrayList<>(), ans);

        return ans;
    }

    private void backtrack(int[] candidates, int target, int start,
                           List<Integer> path, List<List<Integer>> ans) {

        if (target == 0) {
            ans.add(new ArrayList<>(path));
            return;
        }

        for (int i = start; i < candidates.length; i++) {

            // Skip duplicates
            if (i > start && candidates[i] == candidates[i - 1])
                continue;

            // No need to continue
            if (candidates[i] > target)
                break;

            path.add(candidates[i]);

            // i + 1 क्योंकि हर number सिर्फ एक बार use हो सकता है
            backtrack(candidates, target - candidates[i], i + 1, path, ans);

            path.remove(path.size() - 1);
        }
    }
}