p = float(input('Digite seu peso: '))
a = float(input('Digite sua altura: '))
imc = p/(a**2)

if p/(a**2) < 18.5:
    print('\nVocê está ABAIXO do peso!')

elif p/(a**2) >= 18.5 and imc <= 24:
    print('\nVocê está no peso IDEAL!')

elif imc >= 25 and imc <= 30:
    print('\nVocê está SOBREPESO!')

elif imc > 30 and imc <= 40:
    print('\nVocê está na faixa OBESIDADE!')

elif imc > 40:
    print('Você está em OBESIDADE MORBIDA!')