notas = []

while True:
    entrada = input('Digite um número: ')
    if entrada == '-1':
        break
    notas.append(float(entrada))

tamanho = len(notas)
print(f'Foram lidas {tamanho} notas')
print(' '.join([str(nota) for nota in notas]))
notas.reverse()

for nota in notas:
    print(nota)

soma = sum(notas)

print(f'Soma das notas é: {soma}')

media = soma / tamanho
print(f'A média das notas é: {media}')

print('Notas acima de média: ')
print(' '.join([str(nota) for nota in notas if nota > media]))

print('Notas abaixo de 7: ')
print(' '.join([str(nota) for nota in notas if nota < 7]))

print('Encerrado programa de estatística de notas')