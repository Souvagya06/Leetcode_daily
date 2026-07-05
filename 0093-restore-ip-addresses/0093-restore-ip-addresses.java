class Solution {

    List<String> ans = new ArrayList<>();

    public List<String> restoreIpAddresses(String s) {
        backtrack(s, 0, 0, new StringBuilder());
        return ans;
    }

    private void backtrack(String s, int idx, int parts, StringBuilder path) {
        if (parts == 4) {
            if (idx == s.length())
                ans.add(path.substring(0, path.length() - 1));
            return;
        }

        for (int len = 1; len <= 3 && idx + len <= s.length(); len++) {
            String part = s.substring(idx, idx + len);

            if (part.length() > 1 && part.charAt(0) == '0')
                break;

            int val = Integer.parseInt(part);
            if (val > 255)
                break;

            int oldLen = path.length();
            path.append(part).append('.');
            backtrack(s, idx + len, parts + 1, path);
            path.setLength(oldLen);
        }
    }
}