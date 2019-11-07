# lcs length with enumeration of subsequences

from collections import defaultdict
       
def lcs(A, B):
    nA, nB = len(A), len(B)
    dp = [[0 for iB in range(1+nB)] for iA in range(1+nA)]
    predecessors = defaultdict(list)
    for k in range(nA, 0, -1):
        predecessors[k, 0].append((k-1, 0))
    for k in range(nB, 0, -1):
        predecessors[0, k].append((0, k-1))
        
    for i in range(1, 1+nA):
        for j in range(1, 1+nB):
            k = dp[i-1][j-1] + 1 if A[i-1]==B[j-1] else float("-inf")
            max_ = max(k, dp[i-1][j], dp[i][j-1])
            if max_ == k:
                predecessors[i,j].append((i-1, j-1))
            if max_ == dp[i-1][j]:
                predecessors[i,j].append((i-1, j))
            if max_ == dp[i][j-1]:
                predecessors[i,j].append((i, j-1))
            dp[i][j] = max_
    
    def f(i, j, idxs):
        if (i, j) == (0, 0):
            result.append(idxs)
        else:
            for pred in predecessors[i, j]:
                new_idxs = list(idxs)
                if (i, j) == (1+pred[0], 1+pred[1]):
                    new_idxs.append(i-1)
                f(*pred, new_idxs)
    
    result, A_idxs = list(), list()       
    f(nA, nB, A_idxs)
    print(result) #list containing lists of A idxs for reconstruct subsequence
    return dp[nA][nB]

if __name__ == "__main__":
    assert lcs("ac", "ac") == 2
    assert lcs("abcde", "acex") == 3
    assert lcs("cs", "sc") == 1
