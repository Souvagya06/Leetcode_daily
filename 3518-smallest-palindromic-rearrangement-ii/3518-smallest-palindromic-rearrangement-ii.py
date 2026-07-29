from collections import Counter
from math import comb

class Solution:
    LIMIT = 10 ** 6 + 1

    def countPerm(self, freq):
        total = sum(freq)
        ans = 1
        rem = total
        for x in freq:
            if x:
                ans *= comb(rem, x)
                if ans > self.LIMIT:
                    return self.LIMIT
                rem -= x
        return ans

    def smallestPalindrome(self, s: str, k: int) -> str:
        cnt = Counter(s)

        half = [0] * 26
        mid = ""

        for c in range(26):
            ch = chr(ord('a') + c)
            if cnt[ch] % 2:
                mid = ch
            half[c] = cnt[ch] // 2

        if self.countPerm(half) < k:
            return ""

        m = sum(half)
        left = []

        for _ in range(m):
            for c in range(26):
                if half[c] == 0:
                    continue

                half[c] -= 1
                ways = self.countPerm(half)

                if ways >= k:
                    left.append(chr(ord('a') + c))
                    break
                else:
                    k -= ways
                    half[c] += 1

        left = "".join(left)
        return left + mid + left[::-1]