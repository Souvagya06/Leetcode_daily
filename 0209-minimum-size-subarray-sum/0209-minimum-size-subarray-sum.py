class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        total = 0
        ans = len(nums) + 1

        for right in range(len(nums)):
            total += nums[right]

            while total >= target:
                ans = min(ans, right - left + 1)
                total -= nums[left]
                left += 1

        return 0 if ans == len(nums) + 1 else ans