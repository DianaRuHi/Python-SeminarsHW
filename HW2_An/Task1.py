# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

n = float(input('Введите число: '))
sum = 0

# nint = int(n)
# nfloat = n - int(n)

# в вещественной части появляется "мусор" в конце, и я не знаю как от него избавиться численно
# while nint != 0 or nfloat != 0:
    # sum += nint % 10  + int(nfloat * 10)
    # nint = nint // 10
    # nfloat = nfloat * 10 - int(nfloat * 10)

str_nfloat = str(n)
for i in range(len(str_nfloat)):
    if str_nfloat[i] != '.':
        sum += int(str_nfloat[i])

print(sum)
