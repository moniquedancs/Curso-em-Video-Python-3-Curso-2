#Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.

n = 0

while True:
    n = int(input("Quer ver a tabuada de qual valor? "))

    if n < 0:
        print("Você solicitou um número inválido. Encerrando...")
        break

    print("~"*10)
    for c in range (1,11):
        multi = n * c
        print(f"{n} x {c} = {multi}")
    print("~"*10)

