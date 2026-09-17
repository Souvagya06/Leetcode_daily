class Solution {
    public int minSumOfLengths(int[] arr, int target) {
        int n = arr.length;
        int INF = n + 1;

        // best[i] = minimum length of a valid subarray
        // whose ending index is <= i
        int[] best = new int[n];

        for (int i = 0; i < n; i++) {
            best[i] = INF;
        }

        int left = 0;
        int sum = 0;
        int ans = INF;

        for (int right = 0; right < n; right++) {
            sum += arr[right];

            // Shrink window if sum becomes too large
            while (sum > target) {
                sum -= arr[left++];
            }

            // Found a subarray with sum = target
            if (sum == target) {
                int len = right - left + 1;

                // Need another subarray completely before 'left'
                if (left > 0 && best[left - 1] != INF) {
                    ans = Math.min(ans, len + best[left - 1]);
                }

                // Store this subarray as the best one up to 'right'
                best[right] = len;
            }

            // Carry forward the previous best
            if (right > 0) {
                best[right] = Math.min(best[right], best[right - 1]);
            }
        }

        return ans == INF ? -1 : ans;
    }
}