#Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

import random
cont = 0

while True:
    jogador = int(input("Digite um valor: "))
    computador = random.randint(0,10)
    total = jogador + computador
    tipo = " "
    while tipo not in "PpIi":
        tipo = str(input("Par ou ímpar? [P ou I]: ")).strip().upper()
    print(f"Você jogou {jogador} e o computador {computador}. Total de {total}.")

    if tipo == "P":
        if total % 2 == 0:
            cont += 1
            print("Você venceu!")
        else:
            print("Você perdeu!")
            break

    elif tipo == "I":
        if total % 2 == 1:
            cont += 1
            print("Você venceu!")
        else:
            print("Você perdeu!")
            break

    print("Vamos jogar novamente...")

print(f"Você venceu {cont} vezes.")

