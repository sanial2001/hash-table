class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        d = collections.defaultdict(int)
        ans = 0
        for num in nums:
            d[num] = d.get(num, 0) + 1
        for key in d:
            if (key + k) in d:
                ans += d[key] * d[key + k]
        return ans
