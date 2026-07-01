class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort()

        merged = [intervals[0]]

        for start, end in intervals[1:]:

            lastEnd = merged[-1][1]

            if start <= lastEnd:

                merged[-1][1] = max(lastEnd, end)

            else:

                merged.append([start, end])

        return merged