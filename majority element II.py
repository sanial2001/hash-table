class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d = {}
        n = len(nums)

        for num in nums:
            d[num] = d.get(num, 0) + 1

        ans = []
        for key in d:
            if d[key] > n // 3:
                ans.append(key)

        return ans
