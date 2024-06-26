import sys
import os
from time import sleep

sys.path.append('SQL')

from Dados import Verdados

def Transferencias(username):

    while True:

        transferencias = Verdados('transferencias','transferencias',['dia','hora','numeroConta','Montante','descricao'],f"username = '{username}'")

        if len(transferencias) == 0:
            print('Não há movimentos disponíveis para mostrar')
            sleep(3)
            os.system('cls')
            break
        
        else:
            for transferencia in transferencias:
                for i in range(len(transferencia)):

                    if i < len(transferencia) - 1:
                        print(transferencia[i],end=' ')
                    
                    elif i == len(transferencia) - 1:
                        print(transferencia[i])
        
        opcao = input('\nVoltar [0]: ').strip()
        
        os.system('cls')
        if opcao == '0':
            break

    return False