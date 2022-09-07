# Напишите программу для проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

x = int(input('Введите X: ')) != 0
y = int(input('Введите Y: ')) != 0
z = int(input('Введите Z: ')) != 0

if ((x or y or z) == False) == 1 and ((x == False) and (y == False) and (z == False)) == 0:
    answer = False
else:
    answer = True

print('¬(X ⋁ Y ⋁ Z) -> ¬X ⋀ ¬Y ⋀ ¬Z  is ', answer)
