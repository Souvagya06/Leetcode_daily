
import heapq

class Solution:
    def busiestServers(self, k, arrival, load):
        # Segment tree: 1 means server is available
        size = 1
        while size < k:
            size *= 2

        tree = [0] * (2 * size)

        for i in range(k):
            tree[size + i] = 1

        for i in range(size - 1, 0, -1):
            tree[i] = tree[2 * i] + tree[2 * i + 1]

        # Update server availability
        def update(idx, val):
            idx += size
            tree[idx] = val

            idx //= 2
            while idx:
                tree[idx] = tree[2 * idx] + tree[2 * idx + 1]
                idx //= 2

        # Find first available server >= start
        def find(start):
            def search(node, left, right):
                if right < start or tree[node] == 0:
                    return -1

                if left == right:
                    return left

                mid = (left + right) // 2

                res = search(node * 2, left, mid)

                if res != -1:
                    return res

                return search(node * 2 + 1, mid + 1, right)

            return search(1, 0, size - 1)

        # Min heap: (finish_time, server_id)
        busy = []

        count = [0] * k

        for i in range(len(arrival)):

            # Release completed servers
            while busy and busy[0][0] <= arrival[i]:
                finish, server = heapq.heappop(busy)
                update(server, 1)

            # Find preferred available server
            server = find(i % k)

            # Wrap around if necessary
            if server == -1:
                server = find(0)

            # Drop request if all servers are busy
            if server == -1:
                continue

            # Assign request
            count[server] += 1

            update(server, 0)

            heapq.heappush(
                busy,
                (arrival[i] + load[i], server)
            )

        # Return servers with maximum requests
        maximum = max(count)

        return [
            i for i in range(k)
            if count[i] == maximum
        ]
