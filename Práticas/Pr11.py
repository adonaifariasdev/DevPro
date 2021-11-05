# Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
lista = []
for _ in range(10):
    numero = float(input(f'Digite {_+1}o. número: '))
    lista.append(numero)
print(lista)
print()
print(lista[::-1])
print()
lista.sort(reverse=True)
print(lista)

