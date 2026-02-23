valores = list()
num = [1,3, 5, 6, 8 , 10]
num.append(13)
num.sort(reverse=True)
num.insert(2, 0)
del num [2]
num.remove(10)
num.insert(0, 10)
print(num)
print(f'esse lista tem {len(num)}')
if 4 in num:
    num.remove(4)
    print('numero 4 removido')
else:
    print('este valor não existe na lista')

for cont in range(0, 7):
    valores.append(int(input('digite um valor: ')))


#for c, v in num:
#   print(f'na posição {c} encontrei o valor {v}')
print('fim')

