'''Дано число 1≤n≤107 1 <= e n <= e 10^7 1≤n≤107, необходимо найти последнюю цифру n n n-го числа Фибоначчи.

Как мы помним, числа Фибоначчи растут очень быстро, поэтому при их вычислении нужно быть аккуратным с переполнением.
В данной задаче, впрочем, этой проблемы можно избежать, поскольку нас интересует только последняя цифра числа
Фибоначчи: если 0≤a,b≤9 0 <= e a,b <= e 9 0≤a,b≤9 — последние цифры чисел Fi F_i Fi​ и Fi+1 F_{i+1} Fi+1​
соответственно, то (a+b) mod 10 (a+b) \bmod{10} (a+b)mod10 — последняя цифра числа Fi+2 F_{i+2} Fi+2​. '''

def fib(n):
    first = 1
    second = 1
    counter = 2
    if n <= 2:
        return 1
    else:
        while counter < n:
            second += first
            second %= 10
            first = second - first
            first %= 10
            counter += 1
        return second


def main():
    n = int(input())
    print(fib(n))