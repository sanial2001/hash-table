import collections
import heapq


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        d = collections.defaultdict(int)
        for i, item in enumerate(list1):
            d[item] = i

        pq = []
        for i, item in enumerate(list2):
            if item in d:
                heapq.heappush(pq, (d[item] + i, item))

        ans = []
        cnt, res = heapq.heappop(pq)
        ans.append(res)
        while pq:
            i, item = heapq.heappop(pq)
            if i == cnt:
                ans.append(item)
            else:
                break

        return ans
