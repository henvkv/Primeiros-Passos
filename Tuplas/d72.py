contagem = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco',
            'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
            'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze'
            'Dezesseis', 'Dezesete', 'Dezoito', 'Dezenove', 'Vinte')

numero = ''
while True:
    numero = int(input('Digite um número de 0 a 20: '))
    while numero < 0 or numero > 20:
        numero = int(input('Tente novamente. Digite um número de 0 a 20: '))
    
    if numero == 20:
        print(f'\nVocê digitou o número {contagem[numero-1]}!')
    
    else:
        print(f'\nVocê digitou o número {contagem[numero]}!')
    break