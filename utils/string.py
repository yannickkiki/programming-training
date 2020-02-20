from itertools import combinations


def subsequences(s):
    n, result = len(s), list()
    for length in range(n, 0, -1):
        for comb in combinations(s, length):
            result.append(''.join(comb))
    return result

def is_subsequence(x, y):
    x = list(x)
    for letter in y:
        if x and x[0] == letter:
            x.pop(0)

    return not x

# result = subsequences("artificiel")
is_subsequence("bc", "acgebe")

['5', 'qoqqqqqqoo', 'qqqqoqoqqq', 'qqqqqoqqqo', 'qqooqoqqqq', 'qqqooqooqq']
