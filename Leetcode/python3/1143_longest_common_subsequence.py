class Solution:
    def longestCommonSubsequence(self, A, B):
        nA, nB = len(A), len(B)
        dp = [[0 for iB in range(1+nB)] for iA in range(1+nA)]
        for i in range(1, 1+nA):
            for j in range(1, 1+nB):
                k = dp[i-1][j-1] + 1 if A[i-1]==B[j-1] else float("-inf")
                dp[i][j] = max(k, dp[i-1][j], dp[i][j-1])
        return dp[nA][nB]

if __name__=='__main__':
    s = Solution()
    assert s.longestCommonSubsequence("abcde", "ace") == 3
