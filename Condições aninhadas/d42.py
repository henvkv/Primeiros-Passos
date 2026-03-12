print(20*'-=')
print('ANALISADOR DE TRIANGULOS!!')
print(20*'-=')
a = float(input('\nDigite um angulo:'))
b = float(input('Digite o segundo angulo:'))
c = float(input('Digite o terceiro angulo:'))
mm = a
m = b
mm2 = c

if b and c < a:
    mm = b
    mm2 = c
if c and a < b:
    mm = c
    mm2 = a
if b and a < c:
    mm = b
    mm2 = a
if c > a and b:
    m = c
if a > b and c:
    m = a

smm = mm + mm2

if smm > m:
    print(20*'-=')
    print('É possível construir um triangulo!')
    print(20*'-=')
    if a+b+c == a*3:
        print('Ele é um EQUILATERO!')
        print(20*'-=')
    if a == b != c or c == b != a or c == a != b:
        print('Ele é um ISOCELES!')
        print(20*'-=')
    if a != b != c:
        print('Ele é um ESCALENO!')
        print(20*'-=')

else:
    print(20*'-=')
    print('NÃO é possível construir um triangulo!')
    print(20*'-=')
