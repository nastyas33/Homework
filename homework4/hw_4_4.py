def fib(n: int):
    fib_1 = fib_2 = 1
    print(fib_1, fib_2, end=' ')
    for _ in range(2, n):
        fib_1, fib_2 = fib_2, fib_1 + fib_2
        print(fib_2, end=' ')
print (fib(7))

def fib_rec(n):
    if n in (1,2):
        return 1
    return fib_rec(n-1) + fib_rec(n - 2)

print (fib_rec(4))