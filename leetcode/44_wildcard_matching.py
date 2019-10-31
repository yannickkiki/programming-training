from collections import defaultdict


class Solution:
    def isMatch(self, s, p):
        def is_match(s_i, p_i):
            answer = is_tuple_match[(s_i, p_i)]
            if answer:
                return answer
            
            if p_i == len(p):
                answer = s_i==len(s)
                is_tuple_match [(s_i, p_i)] = answer
                return answer
            
            if p[p_i] == "?":
                return is_match(s_i+1, p_i+1)
            elif p[p_i] == "*":
                for s_idx in range(s_i, 1+len(s)):
                    if is_match(s_idx, p_i+1):
                        is_tuple_match [(s_idx, p_i+1)] = True
                        return True
                is_tuple_match [(s_i, p_i)] = False
                return False
            else:
                if s_i<len(s) and p[p_i] == s[s_i]:
                    answer = is_match(s_i+1, p_i+1)
                    is_tuple_match [(s_i+1, p_i+1)] = answer
                    return answer
                is_tuple_match [(s_i, p_i)] = False
                return False
        
        is_tuple_match = defaultdict(lambda: None)
        return is_match(0, 0)
    

if __name__ == '__main__':
    s = Solution()
    assert s.isMatch("aa","a") == False
    assert s.isMatch("aa","*") == True
    assert s.isMatch("cb","?a") == False
    assert s.isMatch("adceb","*a*b") == True
    assert s.isMatch("acdcb","a*c?b") == False
    assert s.isMatch("","*") == True
    assert s.isMatch("aaabbbaabab","a*******b") == True
    assert s.isMatch("aaabbbaabaaaaababaabaaabbabbbbbbbbaabababbabbbaaaaba","a****b") == False
    # assert s.isMatch("aaabbbaabaaaaababaabaaabbabbbbbbbbaabababbabbbaaaaba","a*******b") == False
