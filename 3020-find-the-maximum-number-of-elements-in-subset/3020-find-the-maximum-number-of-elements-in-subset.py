from collections import Counter

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        ans = 1

        # Handle 1 separately
        if 1 in cnt:
            if cnt[1] % 2:
                ans = max(ans, cnt[1])
            else:
                ans = max(ans, cnt[1] - 1)

        for x in list(cnt.keys()):
            if x == 1:
                continue

            cur = x
            length = 0

            while cnt[cur] >= 2:
                length += 2
                if cur * cur > 10**18:
                    break
                cur *= cur

            if cnt[cur] == 1:
                length += 1
            else:
                length -= 1

            ans = max(ans, length)

        return ans