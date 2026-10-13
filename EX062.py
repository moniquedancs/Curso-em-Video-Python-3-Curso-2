#Exercício de PA para mostrar mais de 10 termos.

t = int(input("Digite um termo: "))
r = int(input("Digite uma razão: "))

termo = t
cont = 1


def PA():
    global termo, cont
    while cont <= 10:
        print("{}".format(termo), end=" ")
        print("->" if cont < 10 else "", end=" ")
        termo += r
        cont += 1


PA()

while True:
    per = int(input("\nQuantos termos você quer mostrar a mais (0 para sair)? "))

    if per == 0:
        break

    for i in range(per):
        print("{}".format(termo), end=" ")
        print("->", end=" ")
        termo += r

print("FIM!")