# Faça um programa que leia 5 números e informe o maior número.
maior = 0
for c in range(0, 5):
    num = int(input('Digite um número: '))
    if c == 0:
        maior = num
    else:
        if num > maior:
            maior = num
print(f'O maior número digitado foi {maior}.')