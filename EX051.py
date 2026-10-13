#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

n = int(input("Primeiro termo: "))
r = int(input("Digite a razão: "))
decimo = n + (10 - 1) * r

for c in range(n, decimo, r):
    print(c, end = "->")
print("END")