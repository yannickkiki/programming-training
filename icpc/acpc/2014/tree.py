filename = 'tree.in'
with open(filename, 'r') as f:
    number_of_test_cases = int(f.readline())
    for i in range(number_of_test_cases):
        h, l = map(int, f.readline().strip().split(" "))
        n, result, val = 0, 1, 1
        for p in range(1,h+1):
            val *= 2
            if val>l:
                n = p-1
                break
            result += val
            if val==l:
                n = p
                break
        result += l*(h-n)
        print(f"Case {i+1}: {result}")