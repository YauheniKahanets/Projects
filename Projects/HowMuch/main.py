"""Вашей программе на вход подаются две строки s и t, состоящие из строчных латинских букв.

Выведите одно число – количество вхождений строки t в строку s"""

word = input()
sought = input()
counter = 0
flag = True
part = ''
a = 0
if sought not in word:
    print(counter)
else:
    while a + len(sought) <= len(word):
        part = word[a : (a + len(sought))]
        if sought in part:
            counter += 1
        a += 1
    print(counter)
