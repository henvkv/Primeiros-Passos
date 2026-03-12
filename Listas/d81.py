numeros = []

while True:
    numero = numeros.append(int(input('\nDigite um número: ')))
    numeros.sort(reverse=True)
    
    continuar = str(input('Você deseja continuar? [S/N]: ')).upper()
    while continuar not in 'SN':
        continuar = str(input('Você deseja continuar? [S/N]: ')).upper()
    if continuar == 'N':
        print()
        print('='*30)
        print(f'''Você digitou {len(numeros)} número(s).
Valores em ordem decrescente: {numeros}''')
        
        if numeros.count(5) == 0:
            print('O valor 5 não faz parte da lista!')
            break
        else:
            print('O valor 5 faz parte da lista!')
            break