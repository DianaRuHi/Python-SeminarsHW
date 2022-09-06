# Напишите программу для проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

x = int(input('Введите X: ')) != 0
y = int(input('Введите Y: ')) != 0
z = int(input('Введите Z: ')) != 0

answer = ((x or y or z) == False) == (x == False) and (y == False) and (z == False)
print('¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z  is ', answer)
