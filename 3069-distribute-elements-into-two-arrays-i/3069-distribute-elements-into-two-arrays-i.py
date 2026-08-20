class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        a, b = [nums[0]], [nums[1]]

        for x in nums[2:]:
            (a if a[-1] > b[-1] else b).append(x)

        return a + b