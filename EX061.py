#Aprimoramento de um exercício de PA já feito.

print("Gerador de PA")
print("~"*10)
t = int(input("Digite um termo: "))
r = int(input("Digite uma razão: "))

termo = t
cont = 1

while cont <=10:
    print("{} ->".format(termo), end = " ")
    termo +=r
    cont += 1
print("FIM")
