n_tests = int(input())
for idx_test in range(n_tests):
    list_length = int(input())
    list_ = list(map(int, input().split(" ")))
    cost_total = 0
    for i in range(0, list_length-1):
        elt_min, idx_elt_min = 101, None
        for j in range(i, list_length):
            elt = list_[j]
            if elt < elt_min:
                elt_min, idx_elt_min = elt, j
        list_ = list_[:i] + list_[i:idx_elt_min+1][::-1] + list_[idx_elt_min+1:]
        cost = idx_elt_min - i + 1
        cost_total += cost
    print(f"Case #{1 + idx_test}: {cost_total}")
