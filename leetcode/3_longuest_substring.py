# Exercice 3 - Longuest substring without repeating characters


def lengthOfLongestSubstring(s):
    result, current_substring_size, last_cut_idx = 0, 0, 0
    char_last_idx = dict()
    for idx, c in enumerate(s):
        c_last_idx = char_last_idx.get(c, -1)
        if c_last_idx == -1:
            current_substring_size += 1
        else:
            last_cut_idx = max(c_last_idx, last_cut_idx)
            current_substring_size = idx-last_cut_idx
        char_last_idx[c] = idx
        result = max(result, current_substring_size)
    return result
        

s = "abbaabcabba"
result = lengthOfLongestSubstring(s)
