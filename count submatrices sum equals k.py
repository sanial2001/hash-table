class Solution:
    def solve(self, matrix, target):
        m, n = len(matrix), len(matrix[0])
        t = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                t[i][j] = t[i][j - 1] + matrix[i - 1][j - 1]

        ans = 0
        for j in range(1, n + 1):
            for k in range(j, n + 1):
                d = {0: 1}
                sums = 0
                for i in range(1, m + 1):
                    sums += t[i][k] - t[i][j - 1]
                    ans += d.get(sums - target, 0)
                    d[sums] = d.get(sums, 0) + 1

        return ans
