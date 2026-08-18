class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open = 0
        res = 0

        for ele in s:
            if ele == '(':
                open += 1
            elif open > 0:
                open -= 1
            else:
                res += 1

        return res + open