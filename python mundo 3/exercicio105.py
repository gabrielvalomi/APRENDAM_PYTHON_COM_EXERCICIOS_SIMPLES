def notas(n, sit=True):
    """_summary_

    Args:
        n (_type_): _description_
        sit (bool, optional): _description_. Defaults to True.

    Returns:
        _type_: _description_
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n)/len(n)
    if sit:
        if r['média'] >= 7:
            r['situação'] = 'boa'
        elif r['média'] <= 5:
            r['situação'] = 'razuavel'
        else:
            r['situação'] = 'reprovado'

        return r

    resp = notas(5.5, 2.5, 9.5)
    print(resp)