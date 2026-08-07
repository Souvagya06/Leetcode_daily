class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        FACTORS = {
            0: {},
            1: {},
            2: {2: 1},
            3: {3: 1},
            4: {2: 2},
            5: {5: 1},
            6: {2: 1, 3: 1},
            7: {7: 1},
            8: {2: 3},
            9: {3: 2},
        }

        def factorize(x):
            cnt = {2: 0, 3: 0, 5: 0, 7: 0}
            for p in (2, 3, 5, 7):
                while x % p == 0:
                    cnt[p] += 1
                    x //= p
            return cnt if x == 1 else None

        need = factorize(t)
        if need is None:
            return "-1"

        def digit_count(req):
            req = req.copy()

            c8 = req[2] // 3
            r2 = req[2] % 3

            c9 = req[3] // 2
            r3 = req[3] % 2

            c4 = r2 // 2
            c2 = r2 % 2
            c6 = 0

            if c2 and r3:
                c2 = 0
                r3 = 0
                c6 = 1

            if r3 and c4:
                c2 = 1
                c6 = 1
                r3 = 0
                c4 = 0

            return {
                2: c2,
                3: r3,
                4: c4,
                5: req[5],
                6: c6,
                7: req[7],
                8: c8,
                9: c9,
            }

        def total(cnt):
            return sum(cnt.values())

        def build(cnt):
            res = []
            for d in range(2, 10):
                res.extend(str(d) * cnt[d])
            return "".join(res)

        def sub(a, b):
            return {
                2: max(0, a[2] - b.get(2, 0)),
                3: max(0, a[3] - b.get(3, 0)),
                5: max(0, a[5] - b.get(5, 0)),
                7: max(0, a[7] - b.get(7, 0)),
            }

        prefix = {2: 0, 3: 0, 5: 0, 7: 0}
        for ch in num:
            for p, c in FACTORS[int(ch)].items():
                prefix[p] += c

        zero_pos = num.find("0")
        if zero_pos == -1:
            zero_pos = len(num)
            ok = True
            for p in (2, 3, 5, 7):
                if prefix[p] < need[p]:
                    ok = False
                    break
            if ok:
                return num

        cur = prefix.copy()

        for i in range(len(num) - 1, -1, -1):
            d = int(num[i])

            for p, c in FACTORS[d].items():
                cur[p] -= c

            if i > zero_pos:
                continue

            space = len(num) - i - 1

            for nd in range(d + 1, 10):
                rem = sub(sub(need, cur), FACTORS[nd])
                cnt = digit_count(rem)
                if total(cnt) <= space:
                    return (
                        num[:i]
                        + str(nd)
                        + "1" * (space - total(cnt))
                        + build(cnt)
                    )

        cnt = digit_count(need)
        return "1" * (len(num) + 1 - total(cnt)) + build(cnt)