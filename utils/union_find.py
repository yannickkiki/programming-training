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


if __name__=='__main__':
    arr = [0, 1, 2, 3, 4]
    ds = UnionFind(len(arr))
    ds.unionSet(0, 1)
    ds.unionSet(2, 3)
    ds.unionSet(4, 3)
    assert ds.isSameSet(0, 4) == False
    assert ds.isSameSet(2, 4) == True
    assert ds.numDisjointSets() == 2
    assert ds.sizeOfSet(4) == 3
