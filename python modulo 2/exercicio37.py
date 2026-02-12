 #escreva um programa que leia um nomero e converta para binario octal hexadecimal
num = int(input('digite um nomero inteiro: '))
print('''Escolha uma base para conversão:
[1] conversão para BINARIO
[2] conversão para OCTAL
[3] conversão para HEXIDECIMAL''')
opção = int(input('Sua opção: '))

if opção == 1:
    print('{} convertido para BINARIO é igual a {}'. format(num, bin(num)[2:]))
elif opção == 2:
    print('{}convertido para OCTAL e igual a {}'.format(num, oct(num)[2:]))
elif opção == 3:
    print('{} convertido para HEXIDECIMAL e igual a {}'.format(num, hex(num)[2:]))
else:
    print('opção invalida')

