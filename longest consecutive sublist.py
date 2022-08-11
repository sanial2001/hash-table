class Solution:
    def solve(self, nums):
        n = len(nums)
        ans = 0
        for i in range(n):
            mx, mn = nums[i], nums[i]
            for j in range(i, n):
                mx = max(mx, nums[j])
                mn = min(mn, nums[j])
                if mx - mn == j - i:
                    ans = max(ans, j - i + 1)
        return ans
