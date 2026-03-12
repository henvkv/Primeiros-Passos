while True:
    numero = int(input('Quer ver a tabuada de qual valor? '))
    
    if numero >= 0:
        print('-'*30)
        for t in range (1,11):
            print(f'''{numero} x {t} = {numero*t}''')
        print('-'*30)
    
    else:
        break

print('-'*30)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
print('-'*30)