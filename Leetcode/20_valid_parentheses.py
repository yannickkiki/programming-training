from queue import LifoQueue as Stack

OP = {')': '(', '}': '{', ']': '['}

def isOpen(c):
    return c in OP.values()
        

class Solution:
    def isValid(self, s):
        if not s:
            return True
        
        n = len(s)
        if n%2 == 1:
            return False
        
        q = Stack(maxsize=n)
        for c in s:
            if isOpen(c):
                q.put(c)
            elif q.empty() or OP[c] != q.get():
                return False
        return q.empty()
    
if __name__ == '__main__':
    s = Solution()
    result = s.isValid("){")
