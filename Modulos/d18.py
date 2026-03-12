import math
a = float(input('Digite o angulo:'))
r = math.radians(a)
s = math.sin(r)
c = math.cos(r)
t = math.tan(r)
print('Valor do seno: {:.2f}\nValor do cosseno: {:.2f}\nValor da tangente: {:.2f}'.format(
    s, c, t))
