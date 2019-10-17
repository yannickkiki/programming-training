from math import ceil

class FoundException(Exception):
    pass

with open('G.in', 'r') as f:
    t = int(f.readline().strip())
    for i in range(t):
        k, n = map(int, f.readline().strip().split())
        a, b, c = 0, 0, 0
        a_inf, a_sup = 1+(n//4), ceil(3*n/4)
        try:
            for a in range(a_inf, 1+a_sup):
                b_inf, b_sup = 1+ (a*n//(4*a-n)), ceil(2*a*n/(4*a-n))
                for b in range(b_inf, 1+b_sup):
                    c_num, c_den = a*b*n, 4*a*b-a*n-b*n
                    if c_num%c_den==0:
                        c = c_num//c_den
                        raise FoundException
        except FoundException:
            print(f"{k} {a} {b} {c}")
