class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k % 2 == 0 or k % 5 == 0:
            return -1  # No such number exists if k is divisible by 2 or 5

        num = 0
        for length in range(1, k + 1):
            num = (num * 10 + 1) % k
            if num == 0:
                return length
        return -1