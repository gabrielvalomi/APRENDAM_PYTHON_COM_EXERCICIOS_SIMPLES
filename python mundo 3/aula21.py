#ajuda interativa 
#help()
#help(print)
# ou use o doc
#print(input.__doc__)

#dostrings
def contador(i, f, p):
    c = i
    while c<= f:
        print(f'{c}', end='')
        c = c + p
    print('fim')
contador(2, 10, 2)

#usar docstring em help com """" so colocar as """"""
def contador(i, f, p):
    """_summary_

    Args:
        i (_type_): _description_
        f (_type_): _description_
        p (_type_): _description_
    """
    c = i
    while c<= f:
        print(f'{c}', end='')
        c = c + p
    print('fim')
contador(2, 10, 2)

help(contador)

#parametro opcional usado caso a soma nao tenha algum valor tipo soma(2,4) entao voce coloca def somar(a, b, c= 0) entao se nao tiver valor para c, ele vai ser 0 e nao vai dar erro.
def somar(a, b, c):
    s = a+b+c
    print(f'a soma dos numeros são{s}')

somar(2,7,3)
#ou
somar(a=2, b=7, c=2)

#escopo de variavel aqui vemos que n vale para programa inteiro por estar fora de uma função ou lupim mais x e so ima variavel local por estra em def

def test():
    x=8
    print(f'na função teste, n e igual a {n}')
    print(f'na função teste x e igual a {x}')

n= 2
print(f'na função n, n e ihual a {n}')
#--------
a = 2
def função(b):
    global a
    a = 8
    b = b+4
    c = 2
    print(f' o valor de a é {a}')
    print(f'o valor de b é {b}')
    print(f'o valor de c é {c}')
função(a)
print(f'a fora vale{a}')

# vamos aprender retorno de valores o RETURN 
# ao invez de usar isso 
def soma(a=0, b=0, c=0):
    s = a+b+c
    print(f'a soma dos valores sao {s}')

soma(3,2,5)
soma(2,3)
#use isso
def soma(a=0, b=0, c=0):
    s = a + b +c
    return s

resp1 = soma(3,2,5)
resp2 = soma(2,4)
print(f'a somas deram {resp1}, {resp2}')

