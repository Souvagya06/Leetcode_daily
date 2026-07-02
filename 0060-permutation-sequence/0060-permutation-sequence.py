class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        numbers = [str(i) for i in range(1, n + 1)]

        # factorials
        fact = [1] * (n + 1)
        for i in range(1, n + 1):
            fact[i] = fact[i - 1] * i

        k -= 1  # zero-index

        ans = []

        for i in range(n, 0, -1):
            idx = k // fact[i - 1]
            ans.append(numbers.pop(idx))
            k %= fact[i - 1]

        return "".join(ans)