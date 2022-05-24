class Solution:
    def solve(self, s):
        d = {}
        for i in s:
            d[i] = d.get(i, 0) + 1

        cnt = 0
        for key in d:
            if d[key] % 2 != 0:
                cnt += 1
            if cnt > 1:
                return False
        return True
