class Solution:
    def uniformArray(self, nums1: List[int]) -> bool:
        even = [x for x in nums1 if x % 2 == 0]
        odd = [x for x in nums1 if x % 2 == 1]

        # Already all have the same parity
        if not even or not odd:
            return True

        min_even = min(even)
        min_odd = min(odd)

        # Try making every element even
        possible_even = True

        for x in nums1:
            if x % 2 == 0:
                continue

            # Need x - y to be even, so y must be odd.
            # Also x - y >= 1, so y < x.
            if min_odd >= x:
                possible_even = False
                break

        if possible_even:
            return True

        # Try making every element odd
        possible_odd = True

        for x in nums1:
            if x % 2 == 1:
                continue

            # Need x - y to be odd, so y must be odd.
            if min_odd >= x:
                possible_odd = False
                break

        return possible_odd