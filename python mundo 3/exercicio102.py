def fatorial(n, show=True):
    f =1
    for c in range(n, 0, -1):
        if show:
            c>= 1
            print(f' {c} x ', end='')
        else:
            print(' = ', end='')
        f = f * c
    return f 


print(fatorial(5))