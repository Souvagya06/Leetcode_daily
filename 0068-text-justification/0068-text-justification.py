class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        i = 0

        while i < len(words):
            j = i
            line_len = 0

            # Collect words for current line
            while j < len(words) and line_len + len(words[j]) + (j - i) <= maxWidth:
                line_len += len(words[j])
                j += 1

            num_words = j - i

            # Last line OR only one word
            if j == len(words) or num_words == 1:
                line = " ".join(words[i:j])
                line += " " * (maxWidth - len(line))
            else:
                spaces = maxWidth - line_len
                gaps = num_words - 1

                even = spaces // gaps
                extra = spaces % gaps

                line = ""

                for k in range(gaps):
                    line += words[i + k]
                    line += " " * (even + (1 if k < extra else 0))

                line += words[j - 1]

            res.append(line)
            i = j

        return res