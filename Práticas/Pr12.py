# Faça um programa que leia um número indeterminado de valores, correspondentes a notas,
# encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado).
# Após esta entrada de dados, faça:
# Mostre a quantidade de valores que foram lidos;
# Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
# Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
# Calcule e mostre a soma dos valores;
# Calcule e mostre a média dos valores;
# Calcule e mostre a quantidade de valores acima da média calculada;
# Calcule e mostre a quantidade de valores abaixo de sete;
# Encerre o programa com uma mensagem;

valores = []
qtde_valores_lidos = soma_valores = media_valores = 0
while True:
    num = int(input('Digite um número: '))
    if num == -1:
        break
    else:
        valores.append(num)
        qtde_valores_lidos += 1
        soma_valores += num
print(f'Quantidade de valores que lidos: {qtde_valores_lidos}.')
print(f'Valores na Ordem de entrada: {valores}')
print(f'Valores na Ordem Inversa:')
for v in valores[::-1]:
    print(v)
print(f'A Soma dos valores é: {soma_valores}.')
media_valores = soma_valores / qtde_valores_lidos
print(f'A Média dos valores é: {media_valores}.')
print(f'Os valores acima da média são: ', end='')
for v in valores:
    if v > media_valores:
        print(v, end=' ; ')
print()
print(f'Os valores abaixo de 7 são: ', end='')
for v in valores:
    if v < 7:
        print(v, end=' ; ')
print()
print('<<< FIM DO PROGRAMA >>>')
print('OBRIGADO...VOLTE SEMPRE!!!')


