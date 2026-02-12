sexo = str(input('digite seu sexo [M/F: ]')).strip().upper()[0]
while sexo not in 'MnFf':
    sexo = str(input('dados invalidos, por favor, digite novamente: ')).strip().upper()[0]
print('sexo {} registrado com sucesso'.format(sexo))
    
    #if sexo == 'Mm':
    #    print('sexo masculino registrado com sucesso')
    #if sexo == 'Ff':
    #    print('sexo feminino registrado com sucesso')
    