'''Вашей программе на вход подаются следующие запросы:

    create <namespace> <parent> –  создать новое пространство имен с именем <namespace> внутри пространства <parent>

    add <namespace> <var> – добавить в пространство <namespace> переменную <var>

    get <namespace> <var> – получить имя пространства, из которого будет взята переменная <var> при запросе из
        пространства <namespace>, или None, если такого пространства не существует

        Формат входных данных
    В первой строке дано число n (1 ≤ n ≤ 100) – число запросов.
    В каждой из следующих n строк дано по одному запросу.
    Запросы выполняются в порядке, в котором они даны во входных данных.
    Имена пространства имен и имена переменных представляют из себя строки длины не более 10, состоящие из строчных латинских букв.

        Формат выходных данных
    Для каждого запроса get выведите в отдельной строке его результат.'''


scopes = {'global': {'parent': None, 'variables': list()}}


def create(namesp, arg):
    scopes.update({namesp: {'parent': arg, 'variables': list()}})


def get(namesp, arg):
    for key in scopes:
        if arg in scopes[namesp]['variables']:
            return namesp
        if scopes[namesp]['parent'] is None:
            return None
        else:
            namesp = scopes[namesp]['parent']
            get(namesp, arg)


def add(namesp, arg):
    scopes[namesp]['variables'].append((arg))


a = int(input())
for i in range(a):
    cmd, namesp, arg = input().split()
    if cmd == 'create':
        create(namesp, arg)
    if cmd == 'add':
        add(namesp, arg)
    if cmd == 'get':
        print(get(namesp, arg))
