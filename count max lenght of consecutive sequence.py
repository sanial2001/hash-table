class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d = {}

        # set all numbers to true
        for num in nums:
            d[num] = True

        # mark only the numbers as true which can be the beginning of the sequence rest false
        for num in nums:
            if (num - 1) in d:
                d[num] = False

        # counting the max length of consecutive sequence
        ans = 0
        for num in nums:
            if d[num] == True:
                val, cnt = num, 0
                while val in d:
                    val, cnt = val + 1, cnt + 1
                ans = max(ans, cnt)

        return ans
