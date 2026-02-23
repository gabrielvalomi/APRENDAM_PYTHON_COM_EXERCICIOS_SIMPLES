def leiaint(msg):
    """_summary_

    Args:
        msg (_type_): _description_

    Returns:
        _type_: _description_
    """
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0:31m digite um numero valido.\033[m')
        if ok:
            break
    return valor

n = leiaint('digite um numero: ')
print(f'seu numero e esse {n}')