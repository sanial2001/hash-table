class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        d = {}
        for t in wall:
            sums = 0
            for j in range(len(t) - 1):
                sums += t[j]
                d[sums] = d.get(sums, 0) + 1
        res = 0 if not d else max(d.values())
        return len(wall) - res
