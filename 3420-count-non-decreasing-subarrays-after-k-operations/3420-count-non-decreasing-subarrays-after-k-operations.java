
class Solution {
    public long countNonDecreasingSubarrays(int[] nums, int k) {
        int n = nums.length;
        int LOG = 32 - Integer.numberOfLeadingZeros(n);

        // Prefix sum
        long[] pref = new long[n + 1];

        for (int i = 0; i < n; i++) {
            pref[i + 1] = pref[i] + nums[i];
        }

        // Step 1: Next strictly greater element
        int[] nxt = new int[n];
        int[] stack = new int[n];
        int top = -1;

        for (int i = n - 1; i >= 0; i--) {
            while (top >= 0 && nums[stack[top]] <= nums[i]) {
                top--;
            }

            nxt[i] = (top >= 0) ? stack[top] : n;
            stack[++top] = i;
        }

        // Step 2: Cost of each block
        long[] base = new long[n];

        for (int i = 0; i < n; i++) {
            int j = nxt[i];

            base[i] = (long) nums[i] * (j - i)
                    - (pref[j] - pref[i]);
        }

        // Step 3: Binary lifting
        int[][] jump = new int[LOG][n];
        long[][] cost = new long[LOG][n];

        for (int i = 0; i < n; i++) {
            jump[0][i] = nxt[i];
            cost[0][i] = base[i];
        }

        for (int p = 1; p < LOG; p++) {
            for (int i = 0; i < n; i++) {
                int mid = jump[p - 1][i];

                if (mid < n) {
                    jump[p][i] = jump[p - 1][mid];
                    cost[p][i] = cost[p - 1][i]
                               + cost[p - 1][mid];
                } else {
                    jump[p][i] = n;
                    cost[p][i] = cost[p - 1][i];
                }
            }
        }

        // Step 4: Calculate cost of subarray [l, r]
        long[] kCost = new long[1];

        long answer = 0;

        for (int r = 0; r < n; r++) {
            int left = 0;
            int right = r;
            int best = r + 1;

            while (left <= right) {
                int mid = left + (right - left) / 2;

                long total = 0;
                int cur = mid;

                for (int p = LOG - 1; p >= 0; p--) {
                    int end = jump[p][cur];

                    if (end <= r) {
                        total += cost[p][cur];
                        cur = end;
                    }
                }

                // Remaining partial block
                total += (long) nums[cur] * (r - cur + 1)
                       - (pref[r + 1] - pref[cur]);

                if (total <= k) {
                    best = mid;
                    right = mid - 1;
                } else {
                    left = mid + 1;
                }
            }

            answer += r - best + 1;
        }

        return answer;
    }
}
