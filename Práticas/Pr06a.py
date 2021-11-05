while True:
    try:
        numero = int(input('\033[34mDigite um valor entre 0 e 10: \033[m'))
    except ValueError:
        print('\033[31mDeve ser fornecido um valor inteiro.\033[m')
    else:
        if 0 <= numero <=10:
            print(f'\033[33mO número informado é {numero}.\033[m')
            break
        else:
            print('\033[31mO número deve estar entre 0 e 10.\033[m')