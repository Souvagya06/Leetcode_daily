class Solution:
    def maxProduct(self, n: int) -> int:
        digits = []

        while n > 0:
            digits.append(n % 10)
            n //= 10

        ans = 0

        for i in range(len(digits)):
            for j in range(i + 1, len(digits)):
                ans = max(ans, digits[i] * digits[j])

        return ans