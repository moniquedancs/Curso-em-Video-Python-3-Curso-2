#Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
#A) quantas pessoas tem mais de 18 anos.
#B) quantos homens foram cadastrados.
#C) quantas mulheres tem menos de 20 anos.

maior = 0
homens = 0
mulheres = 0

while True:
    idade = int(input("Digite sua idade: "))
    sexo = " "
    while sexo not in ("M","F"):
        sexo = str(input("Digite seu sexo [F/M]: ")).strip().upper()

    if idade > 18:
        maior += 1

    if sexo == "M":
        homens += 1

    if idade < 20 and sexo == "F":
        mulheres += 1

    perg = " "
    while perg not in ("S","N"):
        perg = input("Deseja continuar? [S/N] ").strip().upper()

    if perg == "N":
        print("Obrigada! Encerrando...")
        break

print(f"A quantidade de pessoas maiores de 18 anos é {maior}.")
print(f"A quantidade de homens cadastrados é de {homens} homens.")
print(f"A quantidade de mulheres com menos de 20 anos é de {mulheres} mulheres.")
