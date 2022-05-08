class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        d = collections.defaultdict(list)

        for i in range(len(nums)):
            for j in range(len(nums[i])):
                d[(i + j)].append(nums[i][j])

        ans = []
        for key in d:
            ans += d[key][::-1]

        return ans
