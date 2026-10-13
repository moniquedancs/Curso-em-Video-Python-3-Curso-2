#Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

num = int(input("Digite um número inteiro: "))
print("Bases de conversão:")
print("[1] BINÁRIO")
print("[2] OCTAL")
print("[3] HEXADECIMAL")

base = int(input("Selecione a base: "))

if base == 1:
    print("{} convertido para binário é igual a {}".format(num, bin(num)))
elif base == 2:
    print("{} convertido para octal é igual a {}".format(num, oct(num)))
elif base == 3:
    print("{} convertido para hexadecimal é igual a {}".format(num, hex(num)))
else:
    print("Inválido. Tente novamente!")