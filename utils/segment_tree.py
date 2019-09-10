class SegmentTree():
    def __init__(self, values):
        self.values = values
        self.store = [0]*(4*self.n_values)
        self._build(1, 0, self.n_values-1)
        
    @property
    def n_values(self):
        return len(self.values)
    
    def _left(self, idx):
        return 2*idx
    
    def _right(self, idx):
        return 1+(2*idx)
    
    def _build(self, idx, left, right):
        """ left and right refer to indexes in self.values list """
        if left == right:
            self.store[idx] = left
        else:
            l_idx, r_idx = self._left(idx), self._right(idx)
            middle = (left+right)//2
            
            self._build(l_idx, left, middle)
            self._build(r_idx, middle+1, right)
            
            idx_l, idx_r = self.store[l_idx], self.store[r_idx]
            
            if self.values[idx_l] < self.values[idx_r]:
                self.store[idx] = idx_l
            else:
                self.store[idx] = idx_r
    
    def _rmq(self, idx, left, right, i, j):
        if left>j or right<i:
            return -1
        if i<=left and j>=right:
            return self.store[idx]
        
        l_idx, r_idx = self._left(idx), self._right(idx)
        middle = (left+right)//2
        idx_l = self._rmq(l_idx, left, middle, i, j)
        idx_r = self._rmq(r_idx, middle+1, right, i, j)
        
        if idx_l == -1:
            return idx_r
        if idx_r == -1:
            return idx_l
        
        if self.values[idx_l] < self.values[idx_r]:
            return idx_l
        else:
            return idx_r
          
    def rmq(self, i, j):
        return self._rmq(1, 0, self.n_values-1, i, j)

if __name__ == '__main__' :
    values = [18, 17, 13, 19, 15, 11, 20]
    st = SegmentTree(values)
    # st.store
    # st.rmq(1, 3) #2
    # st.rmq(4, 6) #5
