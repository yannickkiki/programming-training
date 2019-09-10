class SegmentTree():
    def __init__(self, values):
        self.values = values
        self.store = [0]*(4*self.n_values)
        
    @property
    def n_values(self):
        return len(self.values)
    
    def _left(self, idx):
        return 2*idx
    
    def _right(self, idx):
        return 1+(2*idx)
    
    def _build(self, idx, left, right):
        """ left and right refer to indexes in self.values list """
        if left==right:
            self.store[idx] = left
        else:
            l_idx, r_idx = self._left(idx), self._right(idx)
            middle = (left+right)//2
            
            self._build(l_idx, left, middle)
            self._build(r_idx, middle+1, right)
            
            idx_l, idx_r = self.store[l_idx], self.store[l_idx]
            
            if self.values[idx_l] < self.values[idx_r]:
                self.store[idx] = idx_l
            else:
                self.store[idx] = idx_r
    

            
