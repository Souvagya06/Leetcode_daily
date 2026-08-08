class Solution:
    def validSequence(self, word1: str, word2: str) -> list[int]:
        n = len(word1)
        m = len(word2)

        # last[j] = index in word1 where word2[j] can be matched
        # when matching word2 from right to left.
        last = [-1] * m

        i = n - 1
        j = m - 1

        while i >= 0 and j >= 0:
            if word1[i] == word2[j]:
                last[j] = i
                j -= 1
            i -= 1

        ans = []
        j = 0
        canSkip = True

        for i in range(n):
            if j == m:
                break

            # Normal matching character
            if word1[i] == word2[j]:
                ans.append(i)
                j += 1

            # Use our one allowed mismatch
            elif canSkip:
                # If this is the last character, we can always
                # use the mismatch.
                #
                # Otherwise, word2[j+1:] must still be matchable
                # after index i.
                if j == m - 1 or i < last[j + 1]:
                    ans.append(i)
                    j += 1
                    canSkip = False

        return ans if j == m else []