class Solution:
    def reverse(self, x: int) -> int:
        is_x_pos = True
        if x<0:
            x = -x
            is_x_pos = False
        reversed_x = int(str(x)[::-1])
        if is_x_pos and reversed_x<=2**31-1:
            return reversed_x
        if not is_x_pos and reversed_x<=2**31:
            return -reversed_x
        return 0

