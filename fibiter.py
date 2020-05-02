def fib(n):
    if n < 3:
        return 1
    
    F = [0] * (n + 1)
    print(F)
    F[0] = 0
    F[1] = 1
    F[2] = 1
    
    print(F)
    i = 3
    while i <= n:
        F[i] = F[i - 1] + F[i - 2]
        print(F[i])
        i += 1
        
    return (F)

print(fib(20))
