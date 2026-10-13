#Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#EQUILÁTERO: todos os lados iguais
#ISÓSCELES: dois lados iguais, um diferente
#ESCALENO: todos os lados diferentes

n1 = float(input("Primeiro segmento: "))
n2 = float(input("Segundo segmento: "))
n3 = float(input("Terceiro segmento: "))

if n1 < n1 + n2 and n2 < n1 + n3 and n3 < n1 + n2:
    print("Esse triângulo existe e ele é do tipo ",end='')
    if n1 == n2 == n3: print('EQUILÁTERO')
    elif n1 == n2 or n1 == n3 or n2 == n3: print('ISÓSCELES')
    else: print('ESCALENO')
else:
    print("Esse triângulo não existe.")



