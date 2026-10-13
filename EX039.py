#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

ano = int(input("Digite o ano do seu nascimento: "))
atual = date.today().year
idade = atual - ano

print("Quem nasceu em {} tem {} anos em {}.".format(ano, idade, atual))

if atual - ano == 18:
    print("Está na hora de se alistar.")
elif atual - ano < 18:
    print("Ainda não chegou o momento de se alistar. Falta(m) {} ano(s).".format(18-idade))
elif atual - ano > 18:
    print("Você já deveria ter se alistado. Está {} ano(s) atrasado!".format(idade-18))


