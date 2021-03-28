"""По данным n n n отрезкам необходимо найти множество точек минимального размера, для которого каждый из отрезков
содержит хотя бы одну из точек.

В первой строке дано число 1≤n≤100 отрезков. Каждая из последующих n строк содержит
по два числа 0≤l≤r≤10^9  задающих начало и конец отрезка. Выведите оптимальное число
m точек и сами m точек. Если таких множеств точек несколько, выведите любое из них."""

n = int(input())
section = list()
for x in range(1, n + 1):
    left, right = map(int, input().split())
    if not section:
        section.append(left)
        section.append(right)
    else:
        if section[0] <= left <= section[1]:
            section[0] = left
        if section[0] <= right <= section[1]:
            section[1] = right
if section[0] == section[1]:
    section.pop()
print(len(section))
print(*section)