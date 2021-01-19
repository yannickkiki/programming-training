def squash_stars(pattern):
    result = ""
    is_prec_star = False
    for c in pattern:
        if is_prec_star and c=='*':
            continue
        result += c
        is_prec_star = c=='*'
    return result
    
class Solution: 
    def isMatch(self, s, p):
        def is_match(s_i, p_i):
            if (s_i, p_i) not in memo:
                ans = None
                
                if p_i == len(p):
                    ans = s_i==len(s)
                elif p[p_i] == "?":
                    ans = is_match(s_i+1, p_i+1)
                elif p[p_i] == "*":
                    ans = False
                    for s_idx in range(s_i, 1+len(s)):
                        if is_match(s_idx, p_i+1):
                            ans = True
                            break
                else:
                    ans = s_i<len(s) and p[p_i] == s[s_i] and is_match(s_i+1, p_i+1)
                
                memo[s_i, p_i] = ans
            return memo[s_i, p_i]
        
        p = squash_stars(p)
        memo = dict()
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
    assert s.isMatch("aaabbbaabaaaaababaabaaabbabbbbbbbbaabababbabbbaaaaba","a*b") == False
    assert s.isMatch("aaabbbaabaaaaababaabaaabbabbbbbbbbaabababbabbbaaaaba","a*******b") == False
    assert s.isMatch("babbbbaabababaabbababaababaabbaabababbaaababbababaaaaaabbabaaaabababbabbababbbaaaababbbabbbbbbbbbbaabbb", "b**bb**a**bba*b**a*bbb**aba***babbb*aa****aabb*bbb***a") == False
