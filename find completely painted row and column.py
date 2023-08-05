class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        row, col = collections.defaultdict(list), collections.defaultdict(list)
        d = collections.defaultdict(list)
        m, n = len(mat), len(mat[0])
        for i in range(m):
            for j in range(n):
                d[mat[i][j]] = [i, j]

        for i in range(len(arr)):
            x, y = d[arr[i]]
            row[x].append(i)
            col[y].append(i)
            if len(row[x]) == n or len(col[y]) == m:
                return i
