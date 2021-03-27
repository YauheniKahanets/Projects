"""По данным n n n отрезкам необходимо найти множество точек минимального размера, для которого каждый из отрезков
содержит хотя бы одну из точек.

В первой строке дано число 1≤n≤100 отрезков. Каждая из последующих n строк содержит
по два числа 0≤l≤r≤10^9  задающих начало и конец отрезка. Выведите оптимальное число
m точек и сами m точек. Если таких множеств точек несколько, выведите любое из них."""

n = int(input())
segments = dict()
for x in range(1, n + 1):
    a, b = map(int, input().split())
    s = ''
    for i in range(a, b + 1):
        s += str(i)
        section = set(s)
    segments[x]= sorted(section)
print(segments)