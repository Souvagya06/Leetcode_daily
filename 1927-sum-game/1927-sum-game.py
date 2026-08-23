class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num) // 2
        left_sum = right_sum = 0
        left_q = right_q = 0

        for i, x in enumerate(num):
            if x == '?':
                if i < n:
                    left_q += 1
                else:
                    right_q += 1
            else:
                if i < n:
                    left_sum += int(x)
                else:
                    right_sum += int(x)

        if (left_q + right_q) % 2:
            return True

        return left_sum - right_sum != 9 * (right_q - left_q) // 2