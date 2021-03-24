'''Вашей программе на вход подаются три строки s, a, b, состоящие из строчных латинских букв.
    За одну операцию вы можете заменить все вхождения строки a в строку s на строку b.

Например, s = "abab", a = "ab", b = "ba", тогда после выполнения одной операции строка s перейдет в строку "baba", после
    выполнения двух и операций – в строку "bbaa", и дальнейшие операции не будут изменять строку s.

Необходимо узнать, после какого минимального количества операций в строке s не останется вхождений строки a. Если
    операций потребуется более 1000, выведите Impossible.

Выведите одно число – минимальное число операций, после применения которых в строке s не останется вхождений строки
    a, или Impossible, если операций потребуется более 1000. '''

word = input()
sought = input()
replacement = input()
counter = 0
while True:
    if sought in word:
        counter += 1
        word = word.replace(sought, replacement)
        if counter > 1000:
            print('Impossible')
            break
    else:
        print(counter)
        break