class Solution:
    def similarPairs(self, words: List[str]) -> int:
        d = {}
        for word in words:
            if frozenset(word) in d:
                d[frozenset(word)] += 1
            else:
                d[frozenset(word)] = 1

        # print(d.items())

        res = 0
        for key in d:
            if d[key] > 1:
                res += math.factorial(d[key]) // (math.factorial(d[key] - 2) * 2)

        return res
