class Solution {
    public int lengthOfLongestSubstring(String s) {
        int[] m = new int[128];
        int l = 0, ans = 0;

        for (int r = 0; r < s.length(); r++) {
            char c = s.charAt(r);
            m[c]++;
            while (m[c] > 1) m[s.charAt(l++)]--;
            ans = Math.max(ans, r - l + 1);
        }
        return ans;
    }
}