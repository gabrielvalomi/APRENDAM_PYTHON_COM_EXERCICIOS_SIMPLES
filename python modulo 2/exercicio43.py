peso = float(input('qual e seu pelo? (kg)'))
altura = float(input('qual e sua altura? (m)'))
ims = peso / (altura ** 2)
print('o imc dessa pessoa e de {:.1f}'.format(ims))
if ims < 18.5:
    print('voce esta a baixo do peso normal')
elif ims >= 18.5 and ims <25:
    print ('voce esta no peso ideal')
elif ims >=25 and ims <30:
    print(' voce esta acima do peso')
else:
    print(' procure um medico urgente')
