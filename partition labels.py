import collections


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d = collections.defaultdict()
        for i, ch in enumerate(s):
            d[ch] = i

        ans = []
        prev, mx = -1, -1
        for i, ch in enumerate(s):
            mx = max(mx, d[ch])
            if i == mx:
                ans.append(mx - prev)
                prev = mx

        return ans
