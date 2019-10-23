class Solution:
    def isMatch(self, s, p):
        def is_match(s_i, p_i):
            if p_i==len(p):
                return s_i==len(s)
            pattern, is_star = p[p_i], p_i+1<len(p) and p[p_i+1]=='*'
            if not is_star:
                c = s[s_i] if s_i<len(s) else None
                if pattern in [c, '.']:
                    return is_match(s_i+1, p_i+1)
                else:
                    return False
            else:
                matched = is_match(s_i, p_i+2)
                if matched:
                    return True
                if pattern != '.':
                    while s_i<len(s) and s[s_i]==pattern:
                        if is_match(s_i+1, p_i+2):
                            return True
                        s_i += 1
                    return False
                else:
                    while s_i<len(s):
                        if is_match(s_i+1, p_i+2):
                            return True
                        s_i += 1
                    return False

        return is_match(0, 0)
                
    
if __name__ == '__main__':
    s = Solution()
    result1 = s.isMatch("mississippi", "mis*is*p*.") # False
    result2 = s.isMatch("ab", ".*c") # False
    result3 = s.isMatch("aa", "a") #False
    result4 = s.isMatch("a", "ab*") #True
    result5 = s.isMatch("aa", "a*") #True
    result6 = s.isMatch("ab", ".*") # True
    result7 = s.isMatch("aab", "c*a*b") # True
