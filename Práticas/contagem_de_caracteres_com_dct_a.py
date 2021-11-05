def contar_caracter(s):
    """Função que conta os caracteres de uma string

    Ex:

    >>> contar_caracter('renzo')
    {'e': 1, 'n': 1, 'o': 1, 'r': 1, 'z': 1}
    >>> contar_caracter('banana')
    {'a': 3, 'b': 1, 'n': 2}

    :param s: string a ser contada

    """
    resultado = {}

    for caracter in s:
        contagem = resultado.get(caracter, 0)
        contagem += 1
        resultado[caracter] = contagem

    return resultado



if __name__ == '__main__':
    print(contar_caracter('renzo'))
    print()
    print(contar_caracter('banana'))