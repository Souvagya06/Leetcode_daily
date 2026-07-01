class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        currentSum = nums[0]
        maxSum = nums[0]

        for num in nums[1:]:

            currentSum = max(num, currentSum + num)

            maxSum = max(maxSum, currentSum)

        return maxSum