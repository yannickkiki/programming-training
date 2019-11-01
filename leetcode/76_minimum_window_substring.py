from collections import defaultdict


class Stack:
    def __init__(self):
        self.values = []

    def put(self, element):
        self.values.append(element)

    def get(self):
        return self.values.pop()

    def empty(self):
        return len(self.values) == 0


class Solution:
    def minWindow(self, s, t):
        is_tc, last_tc, nt = defaultdict(lambda: False), dict(), len(t)
        for c in t:
            is_tc[c] = True
            last_tc[c] = -1
        left_idx, right_idx, count_tc = 0, 0, 0
        for idx, c in enumerate(s):
            if is_tc[c]:
                if last_tc[c] == -1:
                    count_tc += 1
                    
                if count_tc == 1:
                    left_idx = idx
                elif count_tc == nt:
                    right_idx == idx
                    
                last_tc[c] = idx
            
    

if __name__ == '__main__':
    s = Solution()
    result = s.minWindow("ADOBECODEBANC", "ABC")
