#Crie um programa que faça o computador jogar Jokenpô com você.

import random
import time

itens = [1,2,3]
computador = random.choice(itens)


print('''Suas opções:
[1] PEDRA
[2] PAPEL
[3] TESOURA''')

opcao = int(input("Qual é a sua opção? "))
time.sleep(1)
print("JO")
time.sleep(1)
print("KEN")
time.sleep(1)
print("PO!")
time.sleep(1)
print("~~"*20)
time.sleep(1)
if computador == 1 and opcao == 2:
    print("Eu escolhi PEDRA e você escolheu PAPEL.")
    time.sleep(1)
    print("~~"*20)
    time.sleep(1)
    print("PERDI!")
elif computador == 1 and opcao == 3:
    print("Eu escolhi PEDRA e você escolheu TESOURA.")
    time.sleep(1)
    print("~~" * 20)
    time.sleep(1)
    print("GANHEI!")
elif computador == 2 and opcao == 1:
    print("Eu escolhi PAPEL e você escolheu PEDRA.")
    time.sleep(1)
    print("~~" * 20)
    time.sleep(1)
    print("GANHEI!")
elif computador == 2 and opcao == 3:
    print("Eu escolhi PAPEL e você escolheu TESOURA.")
    time.sleep(1)
    print("~~" * 20)
    time.sleep(1)
    print("PERDI!")
elif computador == 3 and opcao == 1:
    print("Eu escolhi TESOURA e você escolheu PEDRA.")
    time.sleep(1)
    print("~~" * 20)
    time.sleep(1)
    print("PERDI!")
elif computador == 3 and opcao == 2:
    print("Eu escolhi TESOURA e você escolheu PAPEL.")
    time.sleep(1)
    print("~~" * 20)
    time.sleep(1)
    print("GANHEI!")
else:
    print("Nós escolhemos a mesma coisa!")
    time.sleep(1)
    print("~~" * 20)
    time.sleep(1)
    print("EMPATAMOS!")


