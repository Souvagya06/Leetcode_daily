class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

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

                visited[i] = True
                perm.append(nums[i])

                backtrack()

                perm.pop()
                visited[i] = False

        backtrack()

        return ans