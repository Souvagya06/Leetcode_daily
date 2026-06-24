class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        m = r - l + 1

        if n == 1:
            return m

        # State vector: [up[0], up[1], ..., up[m-1], down[0], ..., down[m-1]]
        # Size 2m x 2m transition matrix
        # new_up[v]   = sum(down[u] for u < v)   -> prefix of down part
        # new_down[v] = sum(up[u]   for u > v)   -> suffix of up part

        size = 2 * m
        # Build transition matrix T
        T = [[0] * size for _ in range(size)]

        for v in range(m):
            # new_up[v] = sum(down[u] for u in 0..v-1)
            for u in range(v):
                T[v][m + u] = 1  # up[v] gets down[u], u < v

            # new_down[v] = sum(up[u] for u in v+1..m-1)
            for u in range(v + 1, m):
                T[m + v][u] = 1  # down[v] gets up[u], u > v

        def mat_mul(A, B):
            sz = len(A)
            C = [[0] * sz for _ in range(sz)]
            for i in range(sz):
                for k in range(sz):
                    if A[i][k] == 0:
                        continue
                    for j in range(sz):
                        C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % MOD
            return C

        def mat_pow(M, p):
            sz = len(M)
            result = [[1 if i == j else 0 for j in range(sz)] for i in range(sz)]  # identity
            while p:
                if p & 1:
                    result = mat_mul(result, M)
                M = mat_mul(M, M)
                p >>= 1
            return result

        # Initial state after placing 1 element:
        # up[v] = 1 for all v (can go up from any value)
        # down[v] = 1 for all v (can go down from any value)
        state = [1] * size  # [up[0..m-1], down[0..m-1]]

        # Apply T^(n-1) times
        Tn = mat_pow(T, n - 1)

        # Multiply matrix by state vector
        final = [0] * size
        for i in range(size):
            for j in range(size):
                final[i] = (final[i] + Tn[i][j] * state[j]) % MOD

        return sum(final) % MOD