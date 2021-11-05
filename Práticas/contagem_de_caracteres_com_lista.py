def contar_caracter(s):
    """Função que conta os caracteres de uma string

    Ex:

    >>> contar_caracter('renzo')
    e: 1
    n: 1
    o: 1
    r: 1
    z: 1
    >>> contar_caracter('banana')
    a: 3
    b: 1
    n: 2

    :param s: string a ser contada

    """
    caracteres_ordenados = sorted(s)

    caracter_anterior = caracteres_ordenados[0]
    contagem = 1

    for caracter in caracteres_ordenados[1:]:
        if caracter == caracter_anterior:
            contagem += 1
        else:
            print(f'{caracter_anterior}: {contagem}')
            caracter_anterior = caracter
            contagem = 1

    print(f'{caracter_anterior}: {contagem}')


if __name__ == '__main__':
    contar_caracter('renzo')
    print()
    contar_caracter('banana')
    