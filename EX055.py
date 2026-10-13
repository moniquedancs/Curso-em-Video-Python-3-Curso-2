#Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

import datetime

maior = 0
menor = 0

for c in range(1,8):
    i = int(input("Em que ano a {}ª pessoa nasceu? ".format(c)))

    if datetime.date.today().year - i >= 18:
        maior += 1
    else:
        menor += 1

print("{} pessoas já atingiram a maioridade, e {} ainda não atingiram." .format(maior,menor))

