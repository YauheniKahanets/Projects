"""По данным n n n отрезкам необходимо найти множество точек минимального размера, для которого каждый из отрезков
содержит хотя бы одну из точек.

В первой строке дано число 1≤n≤100 отрезков. Каждая из последующих n строк содержит
по два числа 0≤l≤r≤10^9  задающих начало и конец отрезка. Выведите оптимальное число
m точек и сами m точек. Если таких множеств точек несколько, выведите любое из них."""

n = int(input())
section = list()
segments = set()
for _ in range(1, n + 1):
    left, right = map(int, input().split())
    if not section:
        section.append(left)
        section.append(right)
    else:
        if left > section[0]:
            section[0] = left
        if right < section[1]:
            section[1] = right
        if left < right < section[0]:
            segments.add(section[0])
            segments.add(section[1])
            section.clear()
            section.append(left)
            section.append(right)
        else:
            if right > left > section[1]:
                segments.add(section[0])
                segments.add(section[1])
                section.clear()
                section.append(left)
                section.append(right)
if len(segments) == 0:
    segments.add(section[0])
    segments.add(section[1])
print(len(segments))
print(*(sorted(segments)))
