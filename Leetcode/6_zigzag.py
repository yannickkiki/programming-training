class Solution:
    def convert(self, s: str, numRows: int) -> str:
        lines, row_idx, coef = [""]*numRows, 0, 1
        for c in s:
            lines[row_idx] += c
            row_idx += coef*1
            if row_idx == numRows:
                row_idx = max(0, row_idx - 2)
                coef = -coef
            elif row_idx == -1:
                row_idx = min(numRows-1, 1)
                coef = -coef
        result = ""
        for line in lines:
            result += line
        return result


if __name__ == '__main__':
    s = Solution()
    result = s.convert("PAYPALISHIRING", 1)
