def fibonacciCiclos(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a

n = 10
ans = fibonacciCiclos(n)
print(ans)
