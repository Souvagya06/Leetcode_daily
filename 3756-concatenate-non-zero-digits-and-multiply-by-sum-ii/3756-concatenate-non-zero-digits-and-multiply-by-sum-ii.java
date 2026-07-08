class Solution {
    public int[] sumAndMultiply(String s, int[][] queries) {
        final int MOD = 1_000_000_007;
        int n = s.length();

        long[] prefixNum = new long[n + 1];
        int[] prefixSum = new int[n + 1];
        int[] prefixCnt = new int[n + 1];
        long[] pow10 = new long[n + 1];

        pow10[0] = 1;
        for (int i = 1; i <= n; i++) {
            pow10[i] = (pow10[i - 1] * 10) % MOD;
        }

        for (int i = 0; i < n; i++) {
            int d = s.charAt(i) - '0';

            prefixSum[i + 1] = prefixSum[i] + d;
            prefixCnt[i + 1] = prefixCnt[i];
            prefixNum[i + 1] = prefixNum[i];

            if (d != 0) {
                prefixCnt[i + 1]++;
                prefixNum[i + 1] = (prefixNum[i] * 10 + d) % MOD;
            }
        }

        int[] ans = new int[queries.length];

        for (int i = 0; i < queries.length; i++) {
            int l = queries[i][0];
            int r = queries[i][1];

            int cnt = prefixCnt[r + 1] - prefixCnt[l];
            int sum = prefixSum[r + 1] - prefixSum[l];

            long x = (prefixNum[r + 1]
                    - prefixNum[l] * pow10[cnt] % MOD
                    + MOD) % MOD;

            ans[i] = (int) (x * sum % MOD);
        }

        return ans;
    }
}