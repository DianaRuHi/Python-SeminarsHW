# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

d_str = input('Введите точность: ')
ind = d_str.index('.')
d_str = d_str[ind + 1:]
d = len(d_str)

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