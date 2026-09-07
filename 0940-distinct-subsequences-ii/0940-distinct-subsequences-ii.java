class Solution {
    public int distinctSubseqII(String s) {
        final long MOD = 1_000_000_007L;

        // last[c] = dp value before the previous occurrence of c
        long[] last = new long[26];

        long dp = 0;

        for (char c : s.toCharArray()) {
            int idx = c - 'a';

            long newDp = (2 * dp + 1 - last[idx]) % MOD;

            if (newDp < 0) {
                newDp += MOD;
            }

            // Save the old dp for this character
            last[idx] = dp + 1;

            dp = newDp;
        }

        return (int) dp;
    }
}