import requests
try:
    retorno = requests.get('http://pudim.com.br/')
except:
    print('\033[1;31mNão consegui acessar o site.. :(\033[m')
else:
    print('\033[1;32mConsegui acessar o site com sucesso!\033[m')
    print(retorno.content)