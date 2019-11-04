from collections import defaultdict


class Solution:
    def minWindow(self, s, t):
        is_tc, last_tc, nt = defaultdict(lambda: False), dict(), len(t)
        for c in t:
            is_tc[c] = True
            last_tc[c] = -1

        left_idx, right_idx, count_tc, memo_s = 0, 0, 0, list()
        for idx, c in enumerate(s):
            if is_tc[c]:
                if last_tc[c] == -1:
                    count_tc += 1
                    
                if count_tc == 1:
                    left_idx = idx
                elif count_tc == nt:
                    right_idx == idx
                    count_tc += 1
                elif count_tc > nt:
                    memo_s[last_tc[c]]["is_deleted"] = True
                    
                    
                last_tc[c] = idx
            memo_s.append({"letter": c, "is_deleted": is_tc[c]})
            
    

if __name__ == '__main__':
    s = Solution()
    result = s.minWindow("ADOBECODEBANC", "ABC")
