# Faça um programa que leia 5 números e informe a soma e a média dos números.
soma = media = 0
for c in range(5):
    num = int(input(f'Digite o {c+1}o. número: '))
    soma += num
media = soma / 5
print(f'Soma é: {soma}.')
print(f'Média é: {media}.')