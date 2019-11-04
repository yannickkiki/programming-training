class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        n = len(obstacleGrid[0])
        
        dp = [1] + [0]*(n-1)
        for i, line in enumerate(obstacleGrid):
            for j, c in enumerate(line):
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0
                elif j >= 1:
                    dp[j] = dp[j-1] + dp[j]
        return dp[n-1]


if __name__=='__main__':
    s = Solution()
    assert s.uniquePathsWithObstacles([[0,0,0], [0,0,0], [0,0,0]]) == 6
    assert s.uniquePathsWithObstacles([[0,0,0], [0,1,0], [0,0,0]]) == 2
    assert s.uniquePathsWithObstacles([[0,0,0], [0,1,0], [0,0,0]]) == 2
    assert s.uniquePathsWithObstacles([[0]]) == 1
    assert s.uniquePathsWithObstacles([[1]]) == 0
    assert s.uniquePathsWithObstacles([[0],[1]]) == 0
    assert s.uniquePathsWithObstacles([[1,0]]) == 0
