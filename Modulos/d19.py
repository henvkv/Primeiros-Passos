import random
import emoji
print(emoji.emojize("Quem a Karoline ama mais? :red_heart:", variant="emoji_type"))
a1 = print('Atual lindo perfeito:')
a2 = print('Atual lindo perfeito:')
a3 = print('Atual lindo perfeito:')
a4 = print('Atual lindo perfeito:')
a = [a1, a2, a3, a4]



e = random.choice(a)
print(emoji.emojize('O homem mais amado por Karoline é: {}! :red_heart:'.format(e)))
