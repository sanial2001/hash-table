class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        m = collections.defaultdict(int)
        res = 0

        for word in words:
            if word[::-1] in m and m[word[::-1]] > 0:
                res += 4
                m[word[::-1]] -= 1
            else:
                m[word] += 1

        for word in words:
            if word[0] == word[1] and m[word] == 1:
                res += 2
                break

        return res
