# Напишите программу, удаляющую из текста все слова, содержащие "абв".

text = input ('Введите текст: ')
lis = [i for i in text.split()]
lis1 = []
for i in lis:
    if not 'абв' in i.lower():
        lis1.append(i)
res = ''
for i in lis1:
    res += i + ' '
print(res)
