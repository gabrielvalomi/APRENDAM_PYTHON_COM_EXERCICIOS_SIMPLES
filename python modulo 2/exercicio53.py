frase = str(input('digite sua frase: ')).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
inverso =''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('temos um palindromo')
else:
    print('não temos um palindromo')
print(junto, inverso)

print(' voçe digitou a frase{}'.format(frase))
