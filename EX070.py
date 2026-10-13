#Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
#A) qual é o total gasto na compra.
#B) quantos produtos custam mais de R$1000.
#C) qual é o nome do produto mais barato.

total = 0
acima_de_mil = 0
n = 0
menor = 0
nome_barato = " "

while True:
    nome = " "
    nome = input("Qual é o nome do produto? ")
    valor = float(input("Qual é o valor do produto? R$"))
    total += valor
    n += 1

    if valor > 1000:
        acima_de_mil += 1

    if n == 1:
        menor = valor
    else:
        if valor < menor:
            menor = valor
            nome_barato = nome


    perg = " "
    while perg not in ("N","S"):
        perg = input("Deseja continuar? [S/N]").strip().upper()

    if perg == "N":
        print("Obrigada! Encerrando...")
        break

print(f"Você gastou um total de {total}.")
print(f"Você comprou {acima_de_mil} produto(s) que custa(m) mais de R$1000,00.")
print(f"O produto mais barato foi {nome_barato}, que custa {valor:.2f}.")
