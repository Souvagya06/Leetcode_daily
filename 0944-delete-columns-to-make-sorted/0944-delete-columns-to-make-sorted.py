from typing import List

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        rows, cols = len(strs), len(strs[0])
        deletions = 0
        
        for col in range(cols):
            for row in range(rows - 1):
                if strs[row][col] > strs[row + 1][col]:
                    deletions += 1
                    break  # no need to check further in this column
        
        return deletions