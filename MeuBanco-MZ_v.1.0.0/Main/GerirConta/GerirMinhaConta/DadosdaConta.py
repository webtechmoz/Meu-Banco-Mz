import sys
import os
from time import sleep

sys.path.append('SQL')

from Dados import Verdados

def dadosdaConta(username):
    
    while True:
        nome, idade, username, bloqueado = Verdados('usuarios','usuarios',['nome','idade','username','bloqueado'],f"username = '{username}'")[0]
        
        if bloqueado == 'FALSE':
            print(f'Idade: {idade} anos\r\nEstado da Conta: Activa\r\nNúmero da Conta: {username}\r\nNome: {nome}')

            opcao = input('\nVoltar (0): ')

            os.system('cls')
            if opcao == '0':
                break
        
        else:
            print('Esta conta não existe ou está bloqueada')
            sleep(3)
            break
    
    os.system('cls')
    return False