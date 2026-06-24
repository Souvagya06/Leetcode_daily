class Solution {
    public boolean isPalindrome(int x) {
        int rev = 0, temp = x;

        if (x < 0) return false;   // negative numbers can't be palindrome

        while (temp > 0) {
            rev = rev * 10 + temp % 10;
            temp /= 10;
        }

        return rev == x;
    }
}
