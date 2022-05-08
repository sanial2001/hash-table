class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        d = {}
        for ch in arr:
            d[ch] = d.get(ch, 0) + 1

        for key in d:
            if d[key] == 1:
                k -= 1
                if k == 0:
                    return key

        return ""
