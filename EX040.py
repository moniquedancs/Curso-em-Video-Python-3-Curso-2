#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
#Média abaixo de 5.0: REPROVADO
#Média entre 5.0 e 6.9: RECUPERAÇÃO
#Média 7.0 ou superior: APROVADO

n1 = float(input("Primeira prova: "))
n2 = float(input("Segunda prova: "))
média = (n1+n2)/2

print("Sua média foi de {:.1f}.".format(média))
if média < 5.0:
    print("REPROVADO!")
elif 5 <= média < 7.0:
    print("RECUPERAÇÃO!")
elif média >= 7.0:
    print("APROVADO!")
