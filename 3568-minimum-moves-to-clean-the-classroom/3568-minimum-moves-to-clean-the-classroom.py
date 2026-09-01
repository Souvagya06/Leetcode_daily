from collections import deque

class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])
        
        start = None
        litter = {}
        k = 0
        
        for i in range(m):
            for j in range(n):
                if classroom[i][j] == 'S':
                    start = (i, j)
                elif classroom[i][j] == 'L':
                    litter[(i, j)] = k
                    k += 1
        
        target = (1 << k) - 1
        
        if target == 0:
            return 0
        
        q = deque()
        q.append((start[0], start[1], 0, energy, 0))
        
        # For each (row, col, mask), store maximum energy reached
        best = {}
        best[(start[0], start[1], 0)] = energy
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        while q:
            r, c, mask, e, moves = q.popleft()
            
            if mask == target:
                return moves
            
            if e == 0:
                continue
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if not (0 <= nr < m and 0 <= nc < n):
                    continue
                
                if classroom[nr][nc] == 'X':
                    continue
                
                ne = e - 1
                nmask = mask
                
                if classroom[nr][nc] == 'R':
                    ne = energy
                
                if (nr, nc) in litter:
                    nmask |= (1 << litter[(nr, nc)])
                
                state = (nr, nc, nmask)
                
                # Only continue if we reach this state with MORE energy
                if state not in best or ne > best[state]:
                    best[state] = ne
                    q.append((nr, nc, nmask, ne, moves + 1))
        
        return -1