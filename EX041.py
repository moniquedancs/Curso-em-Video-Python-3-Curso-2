#A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
#Até 9 anos: MIRIM
#Até 14 anos: INFANTIL
#Até 19 anos: JÚNIOR
#Até 25 anos: SÊNIOR
#Acima de 25 anos: MASTER

import datetime

nasc = int(input("Digite o seu ano de nascimento: "))
hoje = datetime.date.today().year
idade = hoje - nasc

print("Sua idade é {} anos.".format(idade))
if idade <= 9:
    print("Sua categoria é MIRIM.")
elif 9 < idade <= 14:
    print("Sua categoria é INFANTIL.")
elif 14 < idade <= 19:
    print("Sua categoria é JÚNIOR.")
elif 19 < idade <= 25:
    print("Sua categoria é SÊNIOR.")
else:
    print("Sua categoria é MASTER.")

