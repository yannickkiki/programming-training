import itertools

with open('circleland.in', 'r') as f:
    t = int(f.readline().strip())
    for i in range(t):
        n, *corridors_lengths = map(int, f.readline().strip().split())
        acc = [0] + list(itertools.accumulate(corridors_lengths))
        result = 1e10
        for edge_idx in range(n):
            l, r = acc[-1]-acc[edge_idx+1], acc[edge_idx]
            result = min(result, 2*l+r, 2*r+l)
        print(result)
