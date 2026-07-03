from collections import deque
from math import inf

class Solution:
    def findMaxPathScore(self, edges, online, k):
        n = len(online)

        graph = [[] for _ in range(n)]
        indegree = [0] * n
        mx = 0

        for u, v, w in edges:
            graph[u].append((v, w))
            indegree[v] += 1
            mx = max(mx, w)

        # Topological order
        q = deque(i for i in range(n) if indegree[i] == 0)
        topo = []

        while q:
            u = q.popleft()
            topo.append(u)
            for v, _ in graph[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    q.append(v)

        def check(limit):
            dp = [inf] * n
            dp[0] = 0

            for u in topo:
                if dp[u] == inf:
                    continue

                if u != 0 and u != n - 1 and not online[u]:
                    continue

                for v, w in graph[u]:
                    if w < limit:
                        continue

                    if v != n - 1 and not online[v]:
                        continue

                    dp[v] = min(dp[v], dp[u] + w)

            return dp[n - 1] <= k

        lo, hi = 0, mx
        ans = -1

        while lo <= hi:
            mid = (lo + hi) // 2

            if check(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1

        return ans