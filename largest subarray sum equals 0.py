class Solution:
    def maxLen(self, n, arr):
        # Code here
        d = {0: -1}
        sums = 0
        ans = 0
        for i in range(n):
            sums += arr[i]
            if sums in d:
                ans = max(ans, i - d[sums])
            else:
                d[sums] = i
        return ans
