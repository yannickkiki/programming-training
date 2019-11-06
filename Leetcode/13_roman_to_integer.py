VAL = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}


class Solution:
    def romanToInt(self, s):
        result, i, n = 0, 0, len(s)
        while i < n:
            if i < n-1 and VAL[s[i+1]] > VAL[s[i]]:
                result += VAL[s[i+1]] - VAL[s[i]]
                i += 2
            else:
                result += VAL[s[i]]
                i += 1
        return result
    

if __name__ == '__main__':
    s = Solution()
    assert s.romanToInt("MCMXCIV") == 1994
    assert s.romanToInt("III") == 3
