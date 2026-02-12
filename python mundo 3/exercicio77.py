palavras = (
    "computador",
    "engenharia",
    "python",
    "algoritmo",
    "desenvolvimento",
    "teclado",
    "monitor",
    "programacao",
    "internet",
    "dados",
    "estrutura",
    "variavel",
    "funcoes",
    "sistema",
    "rede")
for c in palavras:
    print(f'\nNa palavra {c.upper()} temos', end='')
    for letra in c:
        if letra.lower() in 'aeiou':
            print(f'as vogal do {c} sao {letra}')
print('fim')

