def fibonacciRecursivo(n):
    res = None
    
    if n <= 0:
        res = 0
    elif n == 1:
        res = 1
    else:
        res = fibonacciRecursivo(n - 1) + fibonacciRecursivo(n - 2)
    
    return res

ans = fibonacciRecursivo(10)
print(ans)
