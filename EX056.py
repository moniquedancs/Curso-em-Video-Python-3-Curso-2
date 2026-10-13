#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

nome = []
idade = []
sexo = []

velho_nome = ""
velho_idade = -1 #pois "-1" sempre será superado por qualquer idade.
mulher = 0

for c in range (1,5):
    print("----- {}ª PESSOA -----".format(c))
    nome.append(str(input("Nome: ".format(c))))
    idade.append(int(input("Idade: ".format(c))))
    sexo.append(int(input("[1] FEMININO \n[2] MASCULINO \nSexo: ".format(c))))
for i in range(4):
    # Verifica o homem mais velho
    if sexo[i] == 2 and idade[i] > velho_idade:
        velho_idade = idade[i]
        velho_nome = nome[i]
    # Quantas mulheres com menos de 20 anos
    if sexo[i] == 1 and idade[i] < 20:
        mulher += 1

#Média das idades:
media = sum(idade) / len(idade)

print("O homem mais velho entrevistado é o {}, com {} anos.".format(velho_nome,velho_idade))
print("Existe(m) {} mulher(es) com menos de 20 anos.".format(mulher))
print("A idade média entre os 4 entrevistados é de {} anos.".format(media))


