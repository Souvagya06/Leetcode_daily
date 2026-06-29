class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        # build map: (A, B) -> set of possible tops
        pairs = {}
        for triplet in allowed:
            key = triplet[:2]
            if key not in pairs:
                pairs[key] = set()
            pairs[key].add(triplet[2])

        # backtracking to build from bottom upward
        def backtrack(row: str) -> bool:
            # if we reached the top
            if len(row) == 1:
                return True

            # generate all possible next rows
            next_row_candidates = [""]
            for i in range(len(row) - 1):
                key = row[i:i+2]
                if key not in pairs:
                    return False  # no way to place any block

                possible_tops = pairs[key]

                # grow next_row_candidates
                temp = []
                for prefix in next_row_candidates:
                    for top in possible_tops:
                        temp.append(prefix + top)
                next_row_candidates = temp

            # try building from each candidate next row
            for nxt in next_row_candidates:
                if backtrack(nxt):
                    return True

            return False

        return backtrack(bottom)
