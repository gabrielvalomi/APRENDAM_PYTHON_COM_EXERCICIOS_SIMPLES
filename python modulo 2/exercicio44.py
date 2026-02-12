print('{:^40}'.format('lojas valomi'))
preço = float(input('preçoda compra: r$ '))
print('''forma de pagamento
[1]á vista dinheiro
[2] a vista no cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''' )

opção = int(input(' qual a forma de pagamento'))
if opção == 1:
    total = preço - (preço * 10/100)
elif opção == 2:
    total = preço - (preço *5/100)
    print('sua compra de {:.2f} reais tera {:.2f} de desconto'.format(preço, total))
elif opção == 3:
    total = preço 
    parcela = total / 2
    print('sua compra sera parcelada em 2x de r${:.2f}'.format(parcela))
elif opção == 4:
    total = preço + (preço * 2/100)
    totparc = int(input('quantas parcelas: '))
    parcela = total / totparc
    print(' sua compra sera parcelada em {}x de R${:.2f} com juros'.format(totparc, parcela))
else:
    print('valor invalido:ERRO402')
print ('sua compra de {:.2f} vai custar {:.2f} no final'.format(preço,  total))
