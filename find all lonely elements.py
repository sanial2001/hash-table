class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        d = {}
        for num in nums:
            d[num] = d.get(num, 0) + 1

        ans = []
        for num in nums:
            if d[num] == 1 and (num - 1) not in d and (num + 1) not in d:
                ans.append(num)

        return ans
