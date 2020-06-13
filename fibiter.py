def fib(n):
    if n < 2:
        return 1 
        
    ls = [1, 1]

    for i in range(1, n - 1):
        ls.append(ls[i] + ls[i - 1])
    
    return ls[-1]
