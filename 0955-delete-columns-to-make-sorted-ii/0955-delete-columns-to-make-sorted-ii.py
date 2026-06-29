class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)
        m = len(strs[0])

        # Tracks which adjacent pairs are already strictly sorted
        sorted_prefix = [False] * (n - 1)
        deletions = 0

        for col in range(m):
            conflict = False

            for i in range(n - 1):
                # 🔴 FIX IS HERE: i + 1 (not i + col)
                if not sorted_prefix[i] and strs[i][col] > strs[i + 1][col]:
                    conflict = True
                    break

            if conflict:
                deletions += 1
            else:
                # Update confirmed sorted pairs
                for i in range(n - 1):
                    if not sorted_prefix[i] and strs[i][col] < strs[i + 1][col]:
                        sorted_prefix[i] = True

        return deletions
