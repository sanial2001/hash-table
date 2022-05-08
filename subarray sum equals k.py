class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sums = 0
        ans = 0
        d = {0: 1}
        for i in range(len(nums)):
            sums += nums[i]
            if sums - k in d:
                ans += d[sums - k]
            d[sums] = d.get(sums, 0) + 1
        return ans
