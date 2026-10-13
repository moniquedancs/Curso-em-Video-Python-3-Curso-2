#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = str(input("Sexo [M/F]: ")).strip().upper()

while sexo not in ("M", "F"):
    print("Errado! Digite novamente.")
    sexo = str(input("Sexo [M/F]: ")).strip().upper()

print("Certo, você está cadastrado como {}.".format(sexo))
