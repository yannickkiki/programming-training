def test(n):
    mod=10007
    fib={1:2,2:3}
    if n%2==0:x=0
    else: x=1
    for i in range(3,1001):
        if i%2==0:x=0
        else: x=1
        fib[i] = (fib[i-1] + fib[i-2]+x)%mod
    return(fib[n])

with open('C.in', 'r') as f:
    p=int(f.readline())
    for i in range(p):
        k,n=map(int,f.readline().split())
        print(f"{k} {test(n)}")
