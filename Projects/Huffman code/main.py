"""По данной непустой строке s длины не более 10^4, состоящей из строчных букв латинского алфавита,
постройте оптимальный беспрефиксный код. В первой строке выведите количество различных букв k, встречающихся в
строке, и размер получившейся закодированной строки. В следующих k  строках запишите коды букв в формате "letter:
code". В последней строке выведите закодированную строку. """


word = input()
letters = list(set(word))
counter = dict()
code = dict()
values = list()
j = '0'
huffman = ''
print('letters before', letters)
for letter in letters:
    x = word.count(letter)
    counter[letter] = x

values = list(counter.items())

values.sort(key=lambda i: i[1],reverse=True)
letters.clear()
for i in values:
    letters.append(i[0])

print('letters after', letters)

for letter in letters:
    print(letter)
    if letter == letters[-1] and len(word) != 1:
        code[letter] = j[:-1]
    if len(letters) == 1:
        code[letter] = '0'
    else:
        code[letter] = j
    j = '1' + j
print('code', code)
for letter in word:
    huffman += code[letter]

print(len(letters), len(huffman))
for j in code.keys():
    print(j + ': ' + code[j])
print(huffman)
