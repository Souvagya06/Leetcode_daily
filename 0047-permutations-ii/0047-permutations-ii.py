class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        nums.sort()

        ans = []
        perm = []

        visited = [False] * len(nums)

        def backtrack():

            if len(perm) == len(nums):
                ans.append(perm[:])
                return

            for i in range(len(nums)):

                if visited[i]:
                    continue

                # Skip duplicates
                if i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]:
                    continue

                visited[i] = True
                perm.append(nums[i])

                backtrack()

                perm.pop()
                visited[i] = False

        backtrack()

        return ans