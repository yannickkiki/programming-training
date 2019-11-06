class UnionFind:
    def __init__(self, n):
        self.n = n
        self.rank = [0]*n
        self.parent = list(range(n))
        self.setSizes = [1]*n
        self.numSets = n
        
    def findSet(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.findSet(self.parent[i])
        return self.parent[i]
    
    def isSameSet(self, i, j):
        return self.findSet(i) == self.findSet(j)
    
    def unionSet(self, i, j):
        if not self.isSameSet(i, j):
            x, y = self.findSet(i), self.findSet(j)
            if self.rank[x] > self.rank[y]:
                self.parent[y] = x
                self.setSizes[x] += self.setSizes[y]
            else:
                self.parent[x] = y
                self.setSizes[y] += self.setSizes[x]
                if self.rank[x] == self.rank[y]:
                    self.rank[y] += 1
            self.numSets -= 1
                    
    def numDisjointSets(self):
        return self.numSets
    
    def sizeOfSet(self, i):
        return self.setSizes[self.findSet(i)]
    

class Solution:
    def longestConsecutive(self, nums):
        n, idxs, result = len(nums), dict(), 0
        ds = UnionFind(n)
        for i, num in enumerate(nums):
            if idxs.get(num) is not None:
                continue
            side_nums = [num-1, num+1]
            for side_num in side_nums:
                idx = idxs.get(side_num)
                if idx is not None:
                    ds.unionSet(i, idx)
            result = max(result, ds.sizeOfSet(i))
            idxs[num] = i
        return result


if __name__=="__main__":
    s = Solution()
    assert s.longestConsecutive([1,2,0,1]) == 3
    assert s.longestConsecutive([0, -1]) == 2
    assert s.longestConsecutive([100, 4, 200, 1, 3, 2]) == 4
