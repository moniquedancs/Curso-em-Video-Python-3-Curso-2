#Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

print("Média, maior e menor")
print("~"*10)

cont = 0
soma = 0
maior = 0
menor = 0
continuar = "S"

while continuar == "S":
    n = int(input("Digite um número: "))
    soma += n
    cont += 1

    if cont == 1:
        maior = n
        menor = n

    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n

    continuar = " "
    while continuar not in ("S", "N"):
        continuar = input("Quer continuar? [S/N] ").strip().upper()

media = soma / cont
print("Você leu {} números.".format(cont))
print("A média desses números foi de {}.".format(media))
print("O maior número foi {} e o menor foi {}.".format(maior, menor))
