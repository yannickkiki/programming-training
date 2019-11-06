from collections import Counter, defaultdict


class Solution:
    def minWindow(self, s, t):
        if not s or not t:
            return ""
        
        is_t_char = defaultdict(lambda: False)
        is_t_char.update({char: True for char in t})
        
        required_count, current_count = Counter(t), defaultdict(lambda: 0)
        n_to_match, n_matched = len(required_count), 0
        answer = {"length": float("inf"), "left_idx": 0, "right_idx": 0}
        
        left_idx, right_idx = 0, 0
        while right_idx < len(s):
            c = s[right_idx]
            if is_t_char[c]:
                current_count[c] += 1
                if current_count[c] == required_count[c]:
                    n_matched += 1
            while n_matched == n_to_match:
                window_length = right_idx+1-left_idx
                if window_length < answer["length"]:
                    answer = {"length": window_length, "left_idx": left_idx, "right_idx": right_idx}
                c = s[left_idx]
                if is_t_char[c]:
                    current_count[c] -= 1
                    if current_count[c] < required_count[c]:
                        n_matched -= 1
                left_idx += 1
            right_idx += 1
        
        return "" if answer["length"]==float("inf") else s[answer["left_idx"]:1+answer["right_idx"]] 
            

if __name__ == '__main__':
    s = Solution()
    assert s.minWindow("ADBAACBAB", "BAB") == "BAB"
    assert s.minWindow("ADOBECODEBANC", "BANC") == "BANC"
    assert s.minWindow("a", "aa") == ""
