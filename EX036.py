#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

casa = float(input("Qual é o valor da casa que deseja comprar? R$"))
salario = float(input("Qual é o seu salário? R$"))
tempo = int(input("Em quantos anos você deseja pagar? "))

prestacao = casa /(tempo * 12)

if prestacao < (salario * 0.30):
    print('Empréstimo aprovado!')
else:
    print('Empréstimo negado!')

print("Para uma casa de R${:.2f} com um salário de R${:.2f}, sua prestação mensal seria de {:.2f}.".format(casa,salario,prestacao))
