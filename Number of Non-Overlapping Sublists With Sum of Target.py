class Solution:
    def solve(self, nums, target):
        visit = set()
        visit.add(0)
        ans, sums, prev = 0, 0, 0
        for num in nums:
            sums += num
            prev = sums - target
            if prev in visit:
                ans += 1
                visit = set()
            visit.add(sums)
        return ans
