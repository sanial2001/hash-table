import heapq


class Solution:
    def reorganizeString(self, s: str) -> str:
        d = {}
        for i in s:
            d[i] = d.get(i, 0) + 1

        pq = []
        for key in d:
            heapq.heappush(pq, (-d[key], key))

        res = ''
        cnt, ch = heapq.heappop(pq)
        res += ch
        block = (cnt + 1, ch)

        while len(pq) > 0:
            cnt, ch = heapq.heappop(pq)
            res += ch
            if block[0] < 0:
                heapq.heappush(pq, block)
            block = (cnt + 1, ch)

        if len(res) != len(s):
            return ''
        else:
            return res
