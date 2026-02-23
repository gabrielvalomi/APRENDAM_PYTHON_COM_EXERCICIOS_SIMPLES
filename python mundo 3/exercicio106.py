c = ('\033[m', #0 - sem cor
     '\033[0;30;41m', #1 - vermelhor
     '\033[0;30;42m', #2 - verde
     '\033[0;30;43m', #3 - amarelo
     '\033[0;30;44m', #4 - azul
     '\033[0;30m', #5 - branco
     )



def ajuda(con):
    help(con)

def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('-=* tam')
    print(f'{msg}')
    print('-=*tam')
    print(c[0], end='')

comando = 0
while True:
    titulo('SISTEMA AJUDA PYHELP', 2)
    comando = str(input("função ou biblioteca > "))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ate logo', 4)