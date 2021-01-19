class Solution:
    def myAtoi(self, s):
        digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        result_s = ""
        is_digits_exists = False
        is_signed = False
        for c in s:
            if c in digits:
                result_s += c
                is_digits_exists = True
            else:
                if is_digits_exists:
                    break
                else:
                    if c in ['-', '+']:
                        result_s += c
                        if is_signed:
                            return 0
                        is_signed = True
                    elif c == ' ':
                        if is_signed:
                            return 0
                    else:
                        return 0
        if not is_digits_exists:
            return 0
        result = int(result_s)
        if result<0:
            return max(result, -2147483648)
        else:
            return min(result, 2147483647)
                
    
if __name__ == '__main__':
    s = Solution()
    assert s.myAtoi("- 2") == 0
