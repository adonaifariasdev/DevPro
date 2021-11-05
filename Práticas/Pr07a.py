populacao_a = 80_000
populacao_b = 200_000
taxa_de_crescimento_de_a = 1.03
taxa_de_crescimento_de_b = 1.015
anos = 0

while populacao_a < populacao_b:
    #print(f'############ População no ano {anos} ##########')
    #print(f'A População de A: {populacao_a}.')
    #print(f'A População de B: {populacao_b}.')
    anos += 1
    populacao_a = int(populacao_a * taxa_de_crescimento_de_a)
    populacao_b *= taxa_de_crescimento_de_b
    populacao_b = int(populacao_b)

print(f'############ População no ano {anos} ##########')
print(f'A População de A: {populacao_a}.')
print(f'A População de B: {populacao_b}.')