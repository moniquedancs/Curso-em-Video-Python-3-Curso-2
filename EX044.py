#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#à vista dinheiro/cheque: 10% de desconto
#à vista no cartão: 5% de desconto
#em até 2x no cartão: preço formal
#3x ou mais no cartão: 20% de juros

produto = float(input("Digite o valor do produto: R$"))

print('''Métodos de pagamento:
[1] À vista dinheiro/cheque
[2] À vista no cartão
[3] Em até 2x no cartão
[4] 3x ou mais no cartão''')
opcao = int(input("Digite sua opção: "))

if opcao == 1:
    print("Você optou por pagar à vista no dinheiro ou cheque, e ganhou 10% de desconto. Você pagará R${:.2f}.".format(produto*0.9))
elif opcao == 2:
    print("Você optou por pagar à vista no cartão e ganhou 5% de desconto. Você pagará R${:.2f}.".format(produto*0.95))
elif opcao == 3:
    print('''Você optou por pagar em até 2x no cartão.
Neste caso, não há desconto, e você pagará o preço integral de R${:.2f}.
Parcelando em 2x, cada parcela será de R${:.2f}.'''.format(produto, produto/2))
elif opcao == 4:
    qte = int(input("Em quantas parcelas? "))
    parcela = (produto*1.2)/qte
    print('''Você optou por parcelar em {} vezes.
Essa forma de pagamento acarreta um juros de 20%. 
Então, você pagará um total de R${:.2f}, com parcelas de R${:.2f}.'''.format(qte, produto*1.2, parcela))
else:
    print("Não há essa opção. Tente novamente.")