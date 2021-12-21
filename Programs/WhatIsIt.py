n = 0
for i in range(1, n+1):
    n += i


def recursion(n):
    if n == 1:
        return 1
    return n + recursion(n - 1)
