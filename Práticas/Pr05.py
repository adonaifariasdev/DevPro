# Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor
# do saque e depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis
# serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais.
# O programa não deve se preocupar com a quantidade de notas existentes na máquina.
# Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100,
# uma nota de 50, uma nota de 5 e uma nota de 1;
# Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100,
# uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.
while True:
    saque = int(input('Valor do Saque(R$) '))
    if saque < 10 or saque > 600:
        print('\033[31mValores inválidos. Por favor, digite um valor entre R$10,00 e R$600,00.\033[m')
    else:
        total = saque
        cedula = 100
        total_cedulas = 0
        while True:
            if total >= cedula:
                total -= cedula
                total_cedulas += 1
            else:
                if total_cedulas > 0:
                    print(f'Total {total_cedulas} cédulas de R${cedula}')
                if cedula == 100:
                    cedula = 50
                elif cedula == 50:
                    cedula = 10
                elif cedula == 10:
                    cedula = 5
                elif cedula == 5:
                    cedula = 1
                total_cedulas = 0
                if total == 0:
                    break
        print('<<<FIM DO PROGRAMA>>>')
        break