from sympy import isprime, nextprime
from collections import defaultdict
from math import ceil

primes = [2]

def sp(n):
    original_n = n
    if n==1: return n
    divisor_found = False
    for prime in primes:
        if n%prime==0:
            n = n//prime
            divisor_found = True
            break
    while not divisor_found:
        new_prime = nextprime(primes[-1])
        primes.append(new_prime)
        if n%new_prime==0:
            n = n//new_prime
            divisor_found = True
    if n==1: return original_n
    return n
    
with open('h.in', 'r') as f:
    t = int(f.readline().strip())
    for i in range(t):
        k, n, *a = map(int, f.readline().strip().split())
        precedence_idx = defaultdict(lambda: defaultdict(lambda: -1))
        precedence_idx[a[1]][a[0]] = 1
        m, length, is_repeated, last_occurence =  n, 0, False, -1
        for idx in range(2, n):
            term = sp(a[idx-1] + a[idx-2])
            a.append(term)
            last_occurence = precedence_idx[term][a[idx-1]]
            if last_occurence == -1:
                precedence_idx[term][a[idx-1]] = idx
            else:
                m, length, is_repeated = idx, idx-last_occurence, True
                break
        print(f"{k} {m} {length}")
        if is_repeated:
            terms_to_display = a[last_occurence-1: m+1]
            number_of_lines = ceil(len(terms_to_display)/20)
            for l_idx in range(number_of_lines):
                start = l_idx*20
                print(" ".join(map(str, terms_to_display[start:start+20])))
        else:
            print(sp(a[n-1]+a[n-2]))