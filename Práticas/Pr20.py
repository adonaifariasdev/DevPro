# https://wiki.python.org.br/ExerciciosArquivos
# 1) Faça um programa que leia um arquivo texto contendo uma lista de endereços IP e
# gere um outro arquivo, contendo um relatório dos endereços IP válidos e inválidos.

def validar(ip:str) -> bool:
    numeros = ip.split('.')

    if len(numeros) != 4:
        return False

    for n in numeros:
        if not (0 <= int(n) <= 255):
            return False
    return True

ips_validos = []
ips_invaldios = []
with open('ips.txt', 'r') as arquivo:
    for linha in arquivo:
        ip = linha.strip()
        if validar(ip):
            ips_validos.append(ip)
        else:
            ips_invaldios.append(ip)

with open('ips_saida.txt', 'w') as arquivo:
    arquivo.writelines('[Endereços válidos:]\n')

    for ip in ips_validos:
        arquivo.writelines(f'{ip}\n')

    arquivo.writelines('\n')
    arquivo.writelines('\n')
    arquivo.writelines('[Endereços inválidos:]\n')

    for ip in ips_invaldios:
        arquivo.writelines(f'{ip}\n')
