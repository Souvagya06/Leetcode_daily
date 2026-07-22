from dataclasses import dataclass
from typing import List
import itertools


@dataclass
class Group:
    start: int
    length: int


class SparseTable:
    def __init__(self, nums):
        self.n = len(nums)
        self.st = [[0] * (self.n + 1) for _ in range(self.n.bit_length() + 1)]
        if self.n:
            self.st[0][:self.n] = nums
            for k in range(1, self.n.bit_length() + 1):
                for i in range(self.n - (1 << k) + 1):
                    self.st[k][i] = max(
                        self.st[k - 1][i],
                        self.st[k - 1][i + (1 << (k - 1))]
                    )

    def query(self, l, r):
        k = (r - l + 1).bit_length() - 1
        return max(self.st[k][l], self.st[k][r - (1 << k) + 1])


class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: List[List[int]]) -> List[int]:
        ones = s.count('1')

        zeroGroups, zeroGroupIndex = self.getZeroGroups(s)

        if not zeroGroups:
            return [ones] * len(queries)

        mergeLens = [
            a.length + b.length
            for a, b in itertools.pairwise(zeroGroups)
        ]

        st = SparseTable(mergeLens)

        ans = []

        for l, r in queries:

            left = (
                -1
                if zeroGroupIndex[l] == -1
                else zeroGroups[zeroGroupIndex[l]].length
                - (l - zeroGroups[zeroGroupIndex[l]].start)
            )

            right = (
                -1
                if zeroGroupIndex[r] == -1
                else r - zeroGroups[zeroGroupIndex[r]].start + 1
            )

            startAdj = zeroGroupIndex[l] + 1
            endAdj = (
                zeroGroupIndex[r]
                if s[r] == '1'
                else zeroGroupIndex[r] - 1
            ) - 1

            best = ones

            if (
                s[l] == '0'
                and s[r] == '0'
                and zeroGroupIndex[l] + 1 == zeroGroupIndex[r]
            ):
                best = max(best, ones + left + right)

            elif startAdj <= endAdj and mergeLens:
                best = max(best, ones + st.query(startAdj, endAdj))

            if (
                s[l] == '0'
                and zeroGroupIndex[l] + 1
                <= (
                    zeroGroupIndex[r]
                    if s[r] == '1'
                    else zeroGroupIndex[r] - 1
                )
            ):
                best = max(
                    best,
                    ones
                    + left
                    + zeroGroups[zeroGroupIndex[l] + 1].length,
                )

            if (
                s[r] == '0'
                and zeroGroupIndex[l] < zeroGroupIndex[r] - 1
            ):
                best = max(
                    best,
                    ones
                    + right
                    + zeroGroups[zeroGroupIndex[r] - 1].length,
                )

            ans.append(best)

        return ans

    def getZeroGroups(self, s):
        groups = []
        idx = []

        for i, ch in enumerate(s):
            if ch == '0':
                if i > 0 and s[i - 1] == '0':
                    groups[-1].length += 1
                else:
                    groups.append(Group(i, 1))
            idx.append(len(groups) - 1)

        return groups, idx