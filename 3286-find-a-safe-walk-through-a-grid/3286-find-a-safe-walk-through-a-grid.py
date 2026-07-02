from heapq import heappush, heappop

class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:

        m = len(grid)
        n = len(grid[0])

        INF = float('inf')

        dist = [[INF] * n for _ in range(m)]
        dist[0][0] = grid[0][0]

        heap = [(grid[0][0], 0, 0)]

        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        while heap:

            cost, r, c = heappop(heap)

            if cost > dist[r][c]:
                continue

            if r == m - 1 and c == n - 1:
                return cost < health

            for dr, dc in directions:

                nr = r + dr
                nc = c + dc

                if 0 <= nr < m and 0 <= nc < n:

                    newCost = cost + grid[nr][nc]

                    if newCost < dist[nr][nc]:

                        dist[nr][nc] = newCost
                        heappush(heap, (newCost, nr, nc))

        return False