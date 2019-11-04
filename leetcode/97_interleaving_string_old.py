# not working

class Solution:
    def isInterleave(self, s1, s2, s3):
        p1, n1, p2, n2 = 0, len(s1), 0, len(s2)
        for c in s3:
            print(p1, p2, c)
            if p1 < n1 and s1[p1] == c:
                p1 += 1
            elif p2 < n2 and s2[p2] == c:
                p2 += 1
            else:
                break
        return p1+p2 == len(s3)
            
    

if __name__ == '__main__':
    s = Solution()
    assert s.isInterleave("aabcc", "dbbca", "aadbbcbcac") == True
    assert s.isInterleave("aabcc", "dbbca", "aadbbbaccc") == False
