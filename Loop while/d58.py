import random
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
escolha = random.choice(lista)
palpites = 0

print('\nO COMPUTADOR ESCOLHEU UM NÚMERO DE 1 A 10!')
tentativa = int(input('Qual foi o número escolhido pelo computador? \n'))

while tentativa != escolha:
    print('\nResposta incorreta!')
    tentativa2 = int(input('Digite novamente: '))
    palpites += 1
    
    if tentativa2 == escolha:
        print('\nPARABÉNS, VOCÊ ACERTOU!')
        print(f'Você precisou de {palpites} tentativa para acertar!')
        break
