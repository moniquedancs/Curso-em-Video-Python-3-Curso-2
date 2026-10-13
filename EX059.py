#Crie um programa que leia dois valores e mostre um menu na tela:
#[1] somar, [2] multiplicar, [3] maior, [4] novos números, [5] sair do programa

import time

def menu():
    print("~" * 20)
    print("[1] SOMAR \n[2] MULTIPLICAR \n[3] MOSTRAR O MAIOR \n[4] ADICIONAR NOVOS NÚMEROS \n[5] SAIR DO PROGRAMA")
    print("~" * 20)

n1 = int(input("Digite o primeiro valor: "))
n2 = int(input("Digite o segundo valor: "))
time.sleep(2)

while True:
    time.sleep(4)
    menu ()
    opcoes = int(input("Selecione uma opção: "))
    time.sleep(2)
    print("~" * 20)

    if opcoes == 1:
        soma = n1 + n2
        print("Você escolheu a opção de SOMAR.")
        print("A soma de {} + {} é igual a: {}.".format(n1,n2,soma))

    elif opcoes == 2:
        multi = n1 * n2
        print("Você escolheu a opção de MULTIPLICAR.")
        print("A multiplicação entre {} e {} é igual a: {}.".format(n1,n2,multi))

    elif opcoes == 3:
        print("Você escolheu a opção de COMPARAÇÃO.")
        if n1 > n2:
            print("O número {} é maior que o número {}.".format(n1,n2))
        elif n1 < n2:
            print("O número {} é maior que o número {}.".format(n2,n1))
        else:
            print("Os números {} e {} são iguais.".format(n1,n2))

    elif opcoes == 4:
        print("Você deseja adicionar novos números.")
        n1 = int(input("Digite o primeiro valor: "))
        n2 = int(input("Digite o segundo valor: "))

    elif opcoes == 5:
        print("Você está saindo do programa...")
        break

    else:
        print("Opção inválida!")





