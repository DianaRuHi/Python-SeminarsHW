# Пользователь вводит число, Вам необходимо вывести число Пи 
# с той точностью знаков после запятой, сколько указал пользователь
# (БЕЗ ИСПОЛЬЗОВАНИЯ МОДУЛЕЙ/БИБЛИОТЕК)

d = int (input('Введите точность: '))

def p(d_pi):
    a = 1
    b = 1 / (2 ** (0.5))
    t = 1 / 4
    p = 1
    for i in range(25): #Дает точность pi 45млн знаков
        a, b, t, p = (a+b)/2, (a*b)**(0.5), t-p*(a-(a+b)/2)**2, 2*p
    pi = (a+b)**2/(4*t)
    return ((pi*(10**d_pi))//1)/(10**d_pi) #Дает желаемую точность

print(p(d))