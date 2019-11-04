class Solution:
    def isInterleave(self, s1, s2, s3):
        n1, n2, n3 = len(s1), len(s2), len(s3)
        if n1+n2 != n3:
            return False
        elif n3 == 0:
            return n1 == 0 and n2 == 0

        dp = [False for i2 in range(1+n2)]
        
        for i1 in range(1+n1):
            for i2 in range(1+n2):
                c = s3[i1+i2-1]
                if i1 == 0 and i2 == 0:
                    dp[i2] = True
                elif i1 == 0:
                    dp[i2] = (c == s2[i2-1] and dp[i2-1])
                elif i2 == 0:
                    dp[i2] = (c == s1[i1-1] and dp[i2])
                else:
                    dp[i2] = (c == s2[i2-1] and dp[i2-1]) or (c == s1[i1-1] and dp[i2])
        
        return dp[n2]
                

if __name__ == '__main__':
    s = Solution()
    assert s.isInterleave("", "", "") == True
    assert s.isInterleave("aabcc", "dbbca", "aadbbcbcac") == True
    assert s.isInterleave("aabcc", "dbbca", "aadbbbaccc") == False
    assert s.isInterleave("aabababababababa", "abbabababab", "aabababababababaabbabababab") == True
    result = s.isInterleave("bbbbbabbbbabaababaaaabbababbaaabbabbaaabaaaaababbbababbbbbabbbbababbabaabababbbaabababababbbaaababaa", "babaaaabbababbbabbbbaabaabbaabbbbaabaaabaababaaaabaaabbaaabaaaabaabaabbbbbbbbbbbabaaabbababbabbabaab", "babbbabbbaaabbababbbbababaabbabaabaaabbbbabbbaaabbbaaaaabbbbaabbaaabababbaaaaaabababbababaababbababbbababbbbaaaabaabbabbaaaaabbabbaaaabbbaabaaabaababaababbaaabbbbbabbbbaabbabaabbbbabaaabbababbabbabbab") == False
