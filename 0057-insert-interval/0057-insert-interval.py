class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        result = []

        for interval in intervals:

            # Case 1: Current interval is completely before newInterval
            if interval[1] < newInterval[0]:
                result.append(interval)

            # Case 2: Current interval is completely after newInterval
            elif interval[0] > newInterval[1]:
                result.append(newInterval)
                newInterval = interval

            # Case 3: Overlapping intervals
            else:
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])

        result.append(newInterval)

        return result