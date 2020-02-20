# n = 5
# p = [30, 50, 70, 60, 90]

n = int(input())
p = list(map(lambda item: int(item)/100, input().split(" ")))

p.sort(reverse=True)

memo = [1]
max_expected_value = 0

for i in range(n):
    temp_memo, expected_value = list(), 0
    for j in range(i+2):
        k = 0
        if j > 0: k += p[i]*memo[j-1]
        if j < len(memo): k += (1-p[i])*memo[j]
        temp_memo.append(k)
        term = k*(j**(j/(i+1))) if j!=0 else 0
        expected_value += term
    max_expected_value = max(expected_value, max_expected_value)
    memo = list(temp_memo)
    
print(max_expected_value)
