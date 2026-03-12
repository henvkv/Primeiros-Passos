from datetime import date

a1 = int(input('Digite em que ano você nasceu:'))

aa = date.today().year
a = aa-a1

if a >= 5 and a <= 9:
    print('\nA categoria do atleta é: MIRIM!')

elif a >= 10 and a <= 14:
    print('\nA categoria do atleta é: INFANTIL!')

elif a >= 15 and a <= 19:
    print('\nA categoria do atleta é: JÚNIOR!')

elif a == 20:
    print('\nA categoria do atleta é: SÊNIOR!')

elif a > 20:
    print('\nA categoria do atleta é: MASTER!')

else:
    print('O atleta ainda não pode estar em nenhuma categoria!')
