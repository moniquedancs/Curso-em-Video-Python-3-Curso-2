#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

n = int(input("Digite um número: "))
tot = 0

for d in range(1,n+1):
    if n % d == 0:
        print("\033[33m", end=" ")
        tot += 1
    else:
        print("\033[31m", end=" ")

    print("{}".format(d), end=" ")
print("\n\033[mO número foi divisível {} vezes.".format(tot))

if tot == 2:
    print("É primo.")
else:
    print("Não é primo.")