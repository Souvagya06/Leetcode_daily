class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def is_magic(r, c):
            # Extract 3x3 subgrid
            vals = [grid[r+i][c+j] for i in range(3) for j in range(3)]
            
            # Must contain all numbers 1–9 exactly once
            if sorted(vals) != list(range(1, 10)):
                return False

            # Check sums
            s = 15
            # Rows
            for i in range(3):
                if sum(grid[r+i][c+j] for j in range(3)) != s:
                    return False
            # Columns
            for j in range(3):
                if sum(grid[r+i][c+j] for i in range(3)) != s:
                    return False
            # Diagonals
            if grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2] != s:
                return False
            if grid[r][c+2] + grid[r+1][c+1] + grid[r+2][c] != s:
                return False
            
            return True
        
        m, n = len(grid), len(grid[0])
        count = 0
        
        # Iterate through every top-left corner of a 3x3 window
        for i in range(m - 2):
            for j in range(n - 2):
                if is_magic(i, j):
                    count += 1
        
        return count
