class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = {}
        for num in nums1:
            d[num] = d.get(num, 0) + 1

        ans = []
        for num in nums2:
            if num in d and d[num] > 0:
                ans.append(num)
                d[num] -= 1

        return ans
