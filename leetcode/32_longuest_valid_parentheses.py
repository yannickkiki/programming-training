# from queue import LifoQueue as Stack
class Stack:
    def __init__(self):
        self.values = []
        
    def put(self, element):
        self.values.append(element)
        
    def get(self):
        return self.values.pop()
    
    def empty(self):
        return len(self.values)==0

class Solution:
    def longestValidParentheses(self, s):
        matches = dict()
        q = Stack()
        for idx, c in enumerate(s):
            if c == '(':
                q.put(idx)
            else:
                if not q.empty():
                    matches[q.get()] = idx
        matches = sorted(list(matches.items()))
        result, current_length, last_close_idx = 0, 0, -1
        r = 0
        for open_idx, close_idx in matches:
            if close_idx < r:
                continue
            length = close_idx-open_idx+1
            if last_close_idx == -1:
                current_length = length
            else:
                if open_idx == last_close_idx+1:
                    current_length += length
                else:
                    result = max(result, current_length)
                    current_length = length
            r = last_close_idx = close_idx
        return max(result, current_length)

if __name__ == '__main__':
    s = Solution()
    result0 = s.longestValidParentheses("(()") # 2
    result1 = s.longestValidParentheses(")()())") # 4
    result2 = s.longestValidParentheses("())()") # 2
    result3 = s.longestValidParentheses("(()(()))(()))(") # 12
    result4 = s.longestValidParentheses("())(())()") # 6
