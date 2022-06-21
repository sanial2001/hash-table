class Solution:
    def minDeletions(self, s: str) -> int:
        d = {}
        for i in s:
            d[i] = d.get(i, 0) + 1

        seen = set()
        items = sorted(d.values(), reverse=True)
        ans = 0
        for val in items:
            while val in seen:
                val -= 1
                ans += 1
            if val: seen.add(val)
        return ans
