from collections import defaultdict
from math import ceil

NPG = 10000 
primes = [2]
is_prime = defaultdict(lambda: True)

def extend_primes(previous_max):
    new_max = previous_max+NPG
    for number in range(2, new_max+1):
        if is_prime[number]:
            start = number * ceil(previous_max/number)
            for numberr in range(start, new_max+1, number):
                is_prime[numberr] = False
            if number>previous_max:
                primes.append(number)
    return new_max
            

def sp(n):
    original_n = n
    if n==1: return n
    divisor_found, current_prime_idx, max_number_checked = False, 0, 2
    while not divisor_found:
        while current_prime_idx>=len(primes):
            max_number_checked = extend_primes(max_number_checked)
        new_prime = primes[current_prime_idx]
        if n%new_prime==0:
            n = n//new_prime
            divisor_found = True
        current_prime_idx += 1
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