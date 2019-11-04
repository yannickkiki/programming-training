from collections import Counter


class Solution:
    def minWindow(self, s, t):
        if not s or not t:
            return ""
        
        required_count = Counter(t)
        keys = required_count.keys()
        current_window_count = { t_letter: 0 for t_letter in keys }
        n, left, right, is_desirable, ans = len(s), 0, 0, False, (0, 0)
        is_end = False
        
        while not is_end:
            while not is_desirable:
                if right==n:
                    is_end = True
                    break
                try:
                    current_window_count[s[right]] += 1
                except KeyError:
                    right += 1
                else:
                    right += 1
                    is_desirable = True
                    for key in keys:
                        if current_window_count[key] < required_count[key]:
                            is_desirable = False
                            break
                    if is_desirable:
                        if right-left < ans[1]-ans[0]:
                            ans = (left, right)
                        break
            while is_desirable:
                try:
                    current_window_count[s[left]] -= 1
                except KeyError:
                    left += 1
                else:
                    left += 1
                    is_desirable = True
                    for key in keys:
                        if current_window_count[key] < required_count[key]:
                            is_desirable = False
                            break
                    if not is_desirable:
                        if right==n:
                            left -= 1
                        break
                    if right-left < ans[1]-ans[0]:
                        ans = (left, right)
                    
        return s[left:right]
                    

if __name__ == '__main__':
    s = Solution()
    assert s.minWindow("ADBAACBAB", "BAB") == "BAB"
    assert s.minWindow("ADOBECODEBANC", "BANC") == "BANC"
    assert s.minWindow("a", "aa") == ""
