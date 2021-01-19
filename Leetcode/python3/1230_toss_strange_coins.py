class Solution:
    def probabilityOfHeads(self, prob, target):
        n = len(prob)
        result = [[0 for j in range(target+1)] for i in range(n+1)]
        result[0][0] = 1
        for i in range(1, n+1):
            result[i][0] = result[i-1][0]*(1-prob[i-1])
            for j in range(1, min(i, target)+1):
                result[i][j] = result[i-1][j-1]*prob[i-1]+result[i-1][j]*(1-prob[i-1])
        return result[n][target]

if __name__=='__main__':
    s = Solution()
    val = s.probabilityOfHeads([0.5, 0.5, 0.5], 0)
