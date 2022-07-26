class Solution:
    def solve(self, coordinates):
        ans = 0
        n = len(coordinates)
        for i in range(n):
            d = collections.defaultdict(int)
            for j in range(n):
                if i != j:
                    slope = float("inf")
                    if (coordinates[j][1] - coordinates[i][1]) != 0:
                        slope = (coordinates[j][0] - coordinates[i][0]) / (coordinates[j][1] - coordinates[i][1])
                    d[slope] += 1
            if d:
                ans = max(ans, max(d.values()) + 1)
            else:
                ans = max(ans, 1)

        return ans
