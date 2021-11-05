# Jogo de Forca. Desenvolva um jogo da forca. O programa terá uma lista de palavras lidas de um arquivo texto
# e escolherá uma aleatoriamente. O jogador poderá errar 6 vezes antes de ser enforcado.
# Digite uma letra: A
# -> Você errou pela 1ª vez. Tente de novo!
#
# Digite uma letra: O
# A palavra é: _ _ _ _ O
#
# Digite uma letra: E
# A palavra é: _ E _ _ O
#
# Digite uma letra: S
# -> Você errou pela 2ª vez. Tente de novo!
from random import choice
palavras = ["apple", "banana", "cherry", 'raspberry', 'watermelon', 'Pineapple', 'Blackberry', 'fig', 'Coconut',
        'Cashew', 'Avocado', 'Plum', 'Apricot', 'Guava', 'lime', 'Kiwi fruit', 'Orange', 'Lemon', 'Soursop',
        "Mango", 'Passion fruit', 'Strawberry', 'Peach', 'Pear', 'Grape', 'Tangerine', 'Star fruit', 'Melon', 'DevPro']

palavra = choice(palavras).upper()
print('Jogo da Forca')
print('Descubra a palavra')

print('A palavra é: ', end='')
for letra in palavra:
    print(f'_ ', end='')

conjunto_letras_palavras = set(palavra)
conjunto_letras_digitadas = set()
erros = 0

while not (conjunto_letras_palavras.issubset(conjunto_letras_digitadas)) and erros < 7:
    print()
    print()
    letra_digitada = input('Digite uma letra: ').upper()
    conjunto_letras_digitadas.add(letra_digitada)
    if letra_digitada in conjunto_letras_palavras:
        print('A palavra é: ', end='')
        for letra in palavra:
            if letra in conjunto_letras_digitadas:
                print(f'{letra} ', end='')
            else:
                print(f'_ ', end='')
    else:
        erros += 1
        print(f'-> Erro {erros} de 6. Tente de novo!')

    print()
    print('Letras já digitadas: ', conjunto_letras_digitadas)

if erros < 7:
    print('Parabéns, você ganhou!')
else:
    print('Infelizmente você perdeu!')
