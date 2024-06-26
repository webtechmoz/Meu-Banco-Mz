import sys
import os
from time import sleep

sys.path.append('SQL')

from Dados import Verdados

def Levantamentos(username):

    while True:

        levantamentos = Verdados('levantamentos','levantamentos',['dia','hora','Montante','descricao'],f"username = '{username}'")

        if len(levantamentos) == 0:
            print('Não há movimentos disponíveis para mostrar')
            sleep(3)
            os.system('cls')
            break
        
        else:
            for levantamento in levantamentos:
                for i in range(len(levantamento)):

                    if i < len(levantamento) - 1:
                        print(levantamento[i],end=' ')
                    
                    elif i == len(levantamento) - 1:
                        print(levantamento[i])
        
        opcao = input('\nVoltar [0]: ').strip()
        
        os.system('cls')
        if opcao == '0':
            break

    return False