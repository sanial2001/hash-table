class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        d = {}
        for word in words1:
            d[word] = d.get(word, 0) + 1

        d_copy = d.copy()
        for word in words2:
            if word in d_copy:
                d_copy[word] -= 1

        ans = 0
        for key in d_copy:
            if d_copy[key] == 0 and d[key] == 1:
                ans += 1

        return ans
