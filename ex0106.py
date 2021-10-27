def ajuda():
    from time import sleep
    while True:
        print('\033[1;42m~' * 30)
        print(f'{"SISTEMA DE AJUDA PYHELP":^30}')
        print('~' * 30)
        função = str(input('\033[mFunção da biblioteca: ')).lower().strip()
        if função != 'fim':
            print('\033[m\033[43m~' * 40)
            print(f'Acessando o manual do comando {função}')
            print('~' * 40)
            sleep(1)
            print(f'\033[m\033[5;47m', função.__doc__)
        elif função == 'fim':
            print('\033[m\033[41m~'*20)
            print('FIM')
            print('~'*20)
            break


ajuda()