def fib(n):
    first = 1
    second = 1
    counter = 2
    if n <= 2:
        return 1
    else:
        while counter < n:
            second += first
            first = second - first
            counter += 1
        return second
def main():
    n = int(input())
    print(fib(n))
