def f(n):
    if n <= 2:
        return 1
    return f(n-1) + 3*f(n-2)


print(f(7))