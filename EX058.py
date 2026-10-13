#Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

import random
import time

n = random.randint(0,10)
palpite = 0

escolha = int(input("Pensei em um número entre 1 a 10! Advinhe qual é: "))
palpite += 1

while escolha != n:
    print("PROCESSANDO...")
    time.sleep(1)
    print("\033[4;31mERROU!\033[0m")
    if escolha > n:
        print("É um número menor!")
    else:
        print("É um número maior!")
    escolha = int(input("Pense novamente: "))
    palpite += 1


time.sleep(1)
print("PROCESSANDO...")
time.sleep(1)
print("\033[1;32m----- ACERTOU! -----\033[0m")
print("Eu pensei no número {}.".format(n))
print("E você precisou de {} palpites para acertar.".format(palpite))


