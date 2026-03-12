frase = str(input('Digite uma frase: ')).strip().upper()
separado = frase.split()
junto = ''.join(frase)
inverso = ''

for letra in range(len(junto) -1, -1, -1):
    inverso+=junto[letra]

print('')
print('Ele é um palindromo!' if inverso == junto else 'Ele não é um palindromo!')
print('')