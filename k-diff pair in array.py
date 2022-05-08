class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        d = collections.defaultdict(int)
        ans = 0

        for num in nums:
            d[num] = d.get(num, 0) + 1
        # print(d.items())

        if k == 0:
            for key in d:
                if d[key] > 1:
                    ans += 1
        else:
            for key in d:
                if (key + k) in d:
                    ans += 1

        return ans
