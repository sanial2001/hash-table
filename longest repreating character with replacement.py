class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d = {}
        n = len(s)
        i, ans = 0, 0
        for j in range(n):
            d[s[j]] = d.get(s[j], 0) + 1
            cnt = (j - i + 1) - max(d.values())
            while cnt > k:
                d[s[i]] -= 1
                i = i + 1
                cnt = (j - i + 1) - max(d.values())
            ans = max(ans, j - i + 1)
        return ans
