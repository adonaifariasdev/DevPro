# Faça um programa para imprimir:
#     1
#     1   2
#     1   2   3
#     .....
#     1   2   3   ...  n
# para um n informado pelo usuário. Use uma função que receba um valor n inteiro imprima até a n-ésima linha.

def imprimir_triangulo_de_numeros_crescentes(n: int):
    for linha in range(1, n + 1):
        for coluna in range(1, linha + 1):
            print(coluna, end='   ')
        print('')

num = int(input('Digite um valor(n): '))
imprimir_triangulo_de_numeros_crescentes(num)
