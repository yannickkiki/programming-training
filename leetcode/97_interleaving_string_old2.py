# time limit

class Solution:
    def isInterleave(self, s1, s2, s3):
        if len(s1)+len(s2)!=len(s3):
            return False
        
        def is_inter_leave(p1, p2):
            print(p1, p2)
            if not memo.get((p1, p2)):
                print("generate")
                answer, p3 = False, p1+p2
                if p3 == len(s3):
                    answer = True
                elif p1 < len(s1) and p2 < len(s2) and s3[p3] == s1[p1] == s2[p2]:
                    answer = is_inter_leave(p1+1, p2) or is_inter_leave(p1, p2+1)
                elif p1 < len(s1) and s3[p3] == s1[p1]:
                    answer = is_inter_leave(p1+1, p2)
                elif p2 < len(s2) and s3[p3] == s2[p2]:
                    answer = is_inter_leave(p1, p2+1)
                memo[p1, p2] = answer
            return memo[p1, p2]

        memo = dict()
        return is_inter_leave(0, 0)
            
    

if __name__ == '__main__':
    s = Solution()
    """
    assert s.isInterleave("aabcc", "dbbca", "aadbbcbcac") == True
    assert s.isInterleave("aabcc", "dbbca", "aadbbbaccc") == False
    assert s.isInterleave("aabababababababa", "abbabababab", "aabababababababaabbabababab") == True
    """
    result = s.isInterleave("bbbbbabbbbabaababaaaabbababbaaabbabbaaabaaaaababbbababbbbbabbbbababbabaabababbbaabababababbbaaababaa", "babaaaabbababbbabbbbaabaabbaabbbbaabaaabaababaaaabaaabbaaabaaaabaabaabbbbbbbbbbbabaaabbababbabbabaab", "babbbabbbaaabbababbbbababaabbabaabaaabbbbabbbaaabbbaaaaabbbbaabbaaabababbaaaaaabababbababaababbababbbababbbbaaaabaabbabbaaaaabbabbaaaabbbaabaaabaababaababbaaabbbbbabbbbaabbabaabbbbabaaabbababbabbabbab") == False
