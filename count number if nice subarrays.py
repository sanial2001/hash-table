class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        for i in range(n):
            nums[i] = 0 if nums[i] % 2 == 0 else 1

        d = {0: 1}
        sums, ans = 0, 0
        for i in range(n):
            sums += nums[i]
            if sums - k in d:
                ans += d[sums - k]
            d[sums] = d.get(sums, 0) + 1
        return ans