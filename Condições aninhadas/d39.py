from datetime import date
a = int(input('Digite o ano do seu nascimento:'))

aa = date.today().year
i = aa-a
fi = 18-i
fi2 = i-18

if i < 18:
    print('\nVocê ainda deverá se alistar daqui a {} ano(s)!'.format(fi))

elif i == 18:
    print('\nJá esta na hora de você se alistar!')

elif i > 18:
    print('\nJá se alistou? O prazo para alistamento já passou {} ano(s)!'.format(fi2))
