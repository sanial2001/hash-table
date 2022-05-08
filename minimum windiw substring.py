class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        word, target = {}, {}
        for i in t:
            target[i] = target.get(i, 0) + 1

        have, need, i = 0, len(target), 0
        res, cnt = [-1, -1], float("inf")

        for j, ch in enumerate(s):
            word[ch] = word.get(ch, 0) + 1
            if ch in target and word[ch] == target[ch]:
                have += 1
            while have == need:
                if (j - i + 1) < cnt:
                    cnt = j - i + 1
                    res = [i, j]
                word[s[i]] -= 1
                if s[i] in target and word[s[i]] < target[s[i]]:
                    have -= 1
                i += 1

        return s[res[0]:res[1] + 1]