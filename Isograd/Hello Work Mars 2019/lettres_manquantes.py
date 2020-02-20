#*******
#* Read input from STDIN
#* Use: echo or print to output your result to STDOUT, use the /n constant at the end of each result line.
#* Use: sys.stderr.write() to display debugging information to STDERR
#* ***/
import sys
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

"""
def is_subsequence(l1, l2):
    if l1 == "":
        return True
    elif l2=="":
        return False
    else:
        if l1[0]==l2[0]:
            return contains(l1[1:], l2[1:])
        else:
            return contains(l1, l2[1:])
"""

lines = []
for line in sys.stdin:
	lines.append(line.rstrip('\n'))

sys.stderr.write(str(lines))	
n, ref_word, words = int(lines[0]), lines[1], lines[2:]

subseqs = subsequences(ref_word)

answer = "KO"
for s in subseqs:
    is_found = True
    for word in words:
        if not is_subsequence(s, word):
            is_found = False
            break
    if is_found:
        answer = s
        break
print(answer)