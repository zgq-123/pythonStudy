def a(i, j):
    if i == j:
        print(j)
    else:
        print(i)
        i += 1
        a(i, j)


def b(i, j):
    if i <= j:
        if i == j:
            return j
        else:
            return i + b(i + 1, j)
    else:
        return '输入有误'


def fib_recur(n):
    assert n >= 0, "n > 0"
    if n <= 1:
        return n
    return fib_recur(n - 1) + fib_recur(n - 2)


for i in range(1, 20):
    print(fib_recur(i), end=' ')
# a(1, 100)
# sum = b(2, 10)
# print(sum)
