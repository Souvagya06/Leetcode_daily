from typing import List

class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        count = {}

        # Check every subarray of size k
        for i in range(len(nums) - k + 1):
            seen = set(nums[i:i + k])

            # Count each number only once per subarray
            for x in seen:
                count[x] = count.get(x, 0) + 1

        ans = -1

        for x in count:
            if count[x] == 1:
                ans = max(ans, x)

        return ans