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
            self.store[idx] = self.values[left]
        else:
            l_idx, r_idx = self._left(idx), self._right(idx)
            middle = (left+right)//2
            
            self._build(l_idx, left, middle)
            self._build(r_idx, middle+1, right)
            
            sum_l, sum_r = self.store[l_idx], self.store[r_idx]
            
            self.store[idx] = sum_l + sum_r
    
    def _rsq(self, idx, left, right, i, j):
        if left>j or right<i:
            return 0
        if i<=left and j>=right:
            return self.store[idx]
        
        l_idx, r_idx = self._left(idx), self._right(idx)
        middle = (left+right)//2
        sum_l = self._rsq(l_idx, left, middle, i, j)
        sum_r = self._rsq(r_idx, middle+1, right, i, j)
        
        return sum_l+sum_r
          
    def rsq(self, i, j):
        return self._rsq(1, 0, self.n_values-1, i, j)

if __name__ == '__main__' :
    values = [10, 2, 47, 3, 7, 9, 1, 98, 21]
    st = SegmentTree(values)
    # st.store
    # st.rsq(1, 7) # 167
    # st.rsq(3, 8) # 139
