PHONE = {
    "2": ["a", "b", "c"],
    "3": ["d", "e", "f"],
    "4": ["g", "h", "i"],
    "5": ["j", "k", "l"],
    "6": ["m", "n", "o"],
    "7": ["p", "q", "r", "s"],
    "8": ["t", "u", "v"],
    "9": ["w", "x", "y", "z"]
}

class Solution:
    def letterCombinations(self, digits):
        if not digits:
            return []
        
        result = []
        
        def f(combination, next_digits):
            if not next_digits:
                result.append(combination)
                return
            
            for letter in PHONE[next_digits[0]]:
                f(combination + letter, next_digits[1:])
            
        f("", digits)
        
        return result

if __name__ == '__main__':
    s = Solution()
    result = s.letterCombinations("23")
