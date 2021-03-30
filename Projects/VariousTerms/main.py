"""По данному числу 1≤n≤10^9 найдите максимальное число k, для которого n можно
представить как сумму k различных натуральных слагаемых. Выведите в первой строке число k, во второй — k
слагаемых. """

n = int(input())
result = list()
i = 1
while i <= n:
    result.append(i)
    n -= i
    i += 1
result[-1] += n
print(len(result))
print(*result)
