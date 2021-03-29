"""Первая строка содержит количество предметов 1≤n≤10^3, вместимость рюкзака 0≤W≤2*10^6.
Каждая из следующих n строк задаёт стоимость 0≤ci≤2*10^6 и объём 0<wi≤2*10^6 предмета (n, W, ci, wi — целые числа).
Выведите максимальную стоимость частей предметов (от каждого предмета можно отделить любую часть,
стоимость и объём при этом пропорционально уменьшатся), помещающихся в данный рюкзак, с точностью не менее трёх
знаков после запятой. """


def get_started():
    n, capacity = map(int, input().split())
    items = dict()
    sorted_items = dict()
    for _ in range(n):
        value, size = map(float, input().split())
        items[value/size] = size
    keys = list(items.keys())
    keys.sort(reverse=True)
    for key in keys:
        sorted_items[key] = items[key]
    price = 0
    x = len(sorted_items)
    while capacity > 0 and x != 0:
        for i in sorted_items:
            if capacity > sorted_items[i]:
                price += i * sorted_items[i]
                capacity -= sorted_items[i]
            else:
                price += i * capacity
                capacity = 0
            x -= 1

    return '{:.3f}'.format(price)


print(get_started())
