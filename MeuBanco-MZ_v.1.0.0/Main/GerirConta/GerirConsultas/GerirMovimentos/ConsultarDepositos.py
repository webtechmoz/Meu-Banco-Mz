import sys
import os
from time import sleep

sys.path.append('SQL')

from Dados import Verdados

def Depositos(username):

    while True:

        depositos = Verdados('depositos','depositos',['dia','hora','Montante','descricao'],f"username = '{username}'")

        if len(depositos) == 0:
            print('Não há movimentos disponíveis para mostrar')
            sleep(3)
            os.system('cls')
            break
        
        else:
            for deposito in depositos:
                for i in range(len(deposito)):

                    if i < len(deposito) - 1:
                        print(deposito[i],end=' ')
                    
                    elif i == len(deposito) - 1:
                        print(deposito[i])
        
        opcao = input('\nVoltar [0]: ').strip()
        
        os.system('cls')
        if opcao == '0':
            break

    return False