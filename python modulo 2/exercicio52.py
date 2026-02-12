num = int(input('digite seu numero: '))
tot = 0
for c in range(1, num + 1):
    if num % c ==0:
        print('\033[34m', end=(''))
        tot += 1
    else:
        print('\033[m', end=(''))
    print ('{}'.format(c), end='')
print('\n\033[mO numero {} foi divisivel {} vezes'.format(num, tot))
