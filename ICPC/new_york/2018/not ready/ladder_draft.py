MOD = 10007

v = [0, 1]+[0]*999
r = [0, 1]+[0]*999
l = [0, 0, 0, 1]+[0]*997

for n in range(2, 1001):
    v[n] = r[n-1]
    r[n] = (v[n-1]+r[n-1])%MOD

for n in range(4, 1001):
    sum_ = 0
    for k in range(1, 1+(n//2)):
       sum_ = (sum_ + r[n-2*k-1])%MOD
    l[n] = sum_


with open('_c.in', 'r') as f:
    t = int(f.readline().strip())
    for i in range(t):
        k, val = map(int, f.readline().strip().split())
        result = (v[val]+r[val]+l[val])%MOD
        print(f"{k} {result}")
