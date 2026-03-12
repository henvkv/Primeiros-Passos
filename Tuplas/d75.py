numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite outro número: '))
numero3 = int(input('Digite outro número: '))
numero4 = int(input('Digite outro número: '))

valores = (numero1, numero2, numero3, numero4)

qnt9 = valores.count(9)

print(f'''\nVocê digitou os valores: {valores}
\nO valor 9 apareceu {qnt9} vez(es).''')

if valores.count(3) == 0:
    print('Não contém nenhum número 3.')

else:
    valor3 = valores.index(3)
    print(f'O valor 3 apareceu na {valor3+1}º posição.')

print(f'Os valores pares digitados foram ', end='')

for n in valores:
    if n%2 == 0:
        print(n, end=' ')