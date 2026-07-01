class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        rows = len(matrix)
        cols = len(matrix[0])

        top = 0
        bottom = rows - 1
        left = 0
        right = cols - 1

        ans = []

        while top <= bottom and left <= right:

            # Left -> Right
            for col in range(left, right + 1):
                ans.append(matrix[top][col])
            top += 1

            # Top -> Bottom
            for row in range(top, bottom + 1):
                ans.append(matrix[row][right])
            right -= 1

            # Right -> Left
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    ans.append(matrix[bottom][col])
                bottom -= 1

            # Bottom -> Top
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    ans.append(matrix[row][left])
                left += 1

        return ans