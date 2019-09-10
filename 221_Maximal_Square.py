class Solution221:
    def maximalSquare(self, matrix):

        r = len(matrix)
        if r <= 0:
            return 0
        c = len(matrix[0])
        dp = [0] * c
        m = 0
        for i in range(r):
            prev = dp[0]
            dp[0] = int(matrix[i][0])
            m = max(dp[0], m)
            for j in range(1, c):
                temp = dp[j]
                if matrix[i][j] == '0':
                    dp[j] = 0
                else:
                    dp[j] = min(min(dp[j], dp[j - 1]), prev) + 1

                m = max(m, dp[j])
                prev = temp

        return m * m



S = Solution221()
print(S.maximalSquare([["1","0"]]))
