import java.util.Arrays;

class Solution {
    public int[] gcdValues(int[] nums, long[] queries) {
        int maxVal = 0;
        for (int num : nums) {
            maxVal = Math.max(maxVal, num);
        }

        // Count frequencies of each number
        int[] count = new int[maxVal + 1];
        for (int num : nums) {
            count[num]++;
        }

        // exactGCD[g] will store the exact number of pairs with GCD equal to g
        long[] exactGCD = new long[maxVal + 1];

        // Iterate backwards to compute exact GCD pairs using inclusion-exclusion
        for (int g = maxVal; g >= 1; g--) {
            long multiplesCount = 0;
            for (int multiple = g; multiple <= maxVal; multiple += g) {
                multiplesCount += count[multiple];
            }

            // Total pairs that have 'g' as a common divisor
            long totalPairsWithDivisor = (multiplesCount * (multiplesCount - 1)) / 2;

            // Subtract pairs that have a strictly greater common multiple of g as their GCD
            for (int multiple = 2 * g; multiple <= maxVal; multiple += g) {
                totalPairsWithDivisor -= exactGCD[multiple];
            }

            exactGCD[g] = totalPairsWithDivisor;
        }

        // Build prefix sum array of the counts of GCD values
        long[] prefixSum = new long[maxVal + 1];
        for (int i = 1; i <= maxVal; i++) {
            prefixSum[i] = prefixSum[i - 1] + exactGCD[i];
        }

        // Answer each query using binary search
        int[] answer = new int[queries.length];
        for (int i = 0; i < queries.length; i++) {
            long targetIndex = queries[i];
            
            // Find the smallest GCD 'g' such that prefixSum[g] > targetIndex
            int low = 1, high = maxVal, res = maxVal;
            while (low <= high) {
                int mid = low + (high - low) / 2;
                if (prefixSum[mid] > targetIndex) {
                    res = mid;
                    high = mid - 1;
                } else {
                    low = mid + 1;
                }
            }
            answer[i] = res;
        }

        return answer;
    }
}