''' Огромное число Фибоначчи по модулю
Даны целые числа 1≤n≤10^18  и 2≤m≤10^5, необходимо найти остаток от
 деления n n n-го числа Фибоначчи на m.'''


def fib(n, m):
    fib_list = [0]
    last = 0
    now = 1
    next = last + now
    counter = 0
    for i in range(2, n // 2):
        fib_list.append(next % m)
        last, next = next, (last + next)
        counter += 1
        if last % m == 0 and next % m == 1 and (next + last) % m == 1:
            return fib_list[n % counter]
        if m < counter:
            return n % m


def main():
    n, m = map(int, input().split())
    print(fib(n, m))


main()
