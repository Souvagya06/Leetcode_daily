class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return 1

        pairs = set()

        for i in range(n):
            a = nums[i]
            for j in range(i + 1, n):
                pairs.add(a ^ nums[j])

        ans = set()

        for p in pairs:
            for x in nums:
                ans.add(p ^ x)

        return len(ans)