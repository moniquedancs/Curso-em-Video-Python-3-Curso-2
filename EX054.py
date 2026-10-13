#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

peso = []

for c in range(1,6):
    peso.append(float(input("Peso da {}ª pessoa: ".format(c))))

maior = max(peso)
menor = min(peso)

print("O maior peso lido foi de {:.2f} Kg e o menor peso lido foi de {} Kg.".format(maior,menor))


