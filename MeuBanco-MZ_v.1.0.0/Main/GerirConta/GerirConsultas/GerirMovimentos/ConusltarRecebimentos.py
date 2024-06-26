import sys
import os
from time import sleep

sys.path.append('SQL')

from Dados import Verdados

def Recebimentos(username):

    while True:

        recebimentos = Verdados('recebimentos','recebimentos',['dia','hora','username','Montante','descricao'],f"numeroConta = '{username}'")

        if len(recebimentos) == 0:
            print('Não há movimentos disponíveis para mostrar')
            sleep(3)
            os.system('cls')
            break
        
        else:
            for recebimento in recebimentos:
                for i in range(len(recebimento)):

                    if i < len(recebimento) - 1:
                        print(recebimento[i],end=' ')
                    
                    elif i == len(recebimento) - 1:
                        print(recebimento[i])
        
        opcao = input('\nVoltar [0]: ').strip()
        
        os.system('cls')
        if opcao == '0':
            break

    return False