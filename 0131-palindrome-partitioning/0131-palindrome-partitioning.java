class Solution {

    List<List<String>> ans = new ArrayList<>();
    List<String> path = new ArrayList<>();
    boolean[][] pal;

    public List<List<String>> partition(String s) {

        int n = s.length();
        pal = new boolean[n][n];

        for (int i = n - 1; i >= 0; i--) {
            for (int j = i; j < n; j++) {
                if (s.charAt(i) == s.charAt(j)
                        && (j - i <= 2 || pal[i + 1][j - 1])) {
                    pal[i][j] = true;
                }
            }
        }

        dfs(s, 0);
        return ans;
    }

    private void dfs(String s, int idx) {

        if (idx == s.length()) {
            ans.add(new ArrayList<>(path));
            return;
        }

        for (int end = idx; end < s.length(); end++) {
            if (pal[idx][end]) {
                path.add(s.substring(idx, end + 1));
                dfs(s, end + 1);
                path.remove(path.size() - 1);
            }
        }
    }
}