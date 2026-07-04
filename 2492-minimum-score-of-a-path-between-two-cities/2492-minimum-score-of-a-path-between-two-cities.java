class Solution {

    int ans = Integer.MAX_VALUE;

    public int minScore(int n, int[][] roads) {

        List<int[]>[] graph = new ArrayList[n + 1];

        for (int i = 1; i <= n; i++)
            graph[i] = new ArrayList<>();

        for (int[] road : roads) {
            graph[road[0]].add(new int[]{road[1], road[2]});
            graph[road[1]].add(new int[]{road[0], road[2]});
        }

        boolean[] visited = new boolean[n + 1];

        dfs(1, graph, visited);

        return ans;
    }

    private void dfs(int node, List<int[]>[] graph, boolean[] visited) {

        visited[node] = true;

        for (int[] next : graph[node]) {

            ans = Math.min(ans, next[1]);

            if (!visited[next[0]]) {
                dfs(next[0], graph, visited);
            }
        }
    }
}