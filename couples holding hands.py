class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        d = collections.defaultdict(int)
        n = len(row)

        for i in range(0, n, 2):
            d[row[i]] = row[i + 1]
            d[row[i + 1]] = row[i]

        ans = 0
        for i in range(0, n, 2):
            if d[i] != i + 1:
                l, r = d[i], d[i + 1]
                d[l], d[r] = r, l
                ans += 1

        return ans
