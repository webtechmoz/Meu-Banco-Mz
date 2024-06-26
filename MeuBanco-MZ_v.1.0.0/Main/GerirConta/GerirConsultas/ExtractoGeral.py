import sys
import os

sys.path.append('SQL')

from Dados import Verdados

def extractoGeral(username):

    while True:

        depositos = Verdados('depositos','depositos',['dia','hora','Montante','descricao'],f"username = '{username}'")
        levantamentos = Verdados('levantamentos','levantamentos',['dia','hora','Montante','descricao'],f"username = '{username}'")
        transferencias = Verdados('transferencias','transferencias',['dia','hora','numeroConta','Montante','descricao'],f"username = '{username}'")
        recebimentos = Verdados('recebimentos','recebimentos',['dia','hora','username','Montante','descricao'],f"numeroConta = '{username}'")


        movimentos = [depositos,levantamentos,transferencias,recebimentos]

        for i,movimento in enumerate(movimentos):

            if i == 0:
                print('1 - DEPÓSITOS\n')
            
            elif i == 1:
                print('\n2 - LEVANTAMENTOS\n')

            elif i == 2:
                print('\n3 - TRANSFERÊNCIAS\n')
            
            elif i == 3:
                print('\n4 - RECEBIMENTOS\n')
            
            
            if len(movimento) == 0:
                print('     Sem movimentos disponíveis para mostrar')
            
            else:
                for operacao in movimento:
                    for j in range(len(operacao)):
                        if j < len(operacao) - 1:
                            print(operacao[j],end=' ')
                        
                        elif j == len(operacao) - 1:
                            print(operacao[j])
            
            print()
        

        opcao = input('Voltar [0]: ')
        
        os.system('cls')
        if opcao == '0':
            break
    
    return False