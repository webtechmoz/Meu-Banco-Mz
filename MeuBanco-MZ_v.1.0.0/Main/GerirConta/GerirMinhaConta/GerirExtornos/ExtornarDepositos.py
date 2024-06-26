import sys
import os
from time import sleep

sys.path.append('SQL')

from Dados import Verdados, ApaharLinha, ActualizarDados

def extornarDepositos(username):

    saldo = Verdados('saldo','saldo',['Montante'],f"username = '{username}'")[0][0]

    if saldo == 0:
        print('Não tem saldo disponível para efectuar extorno de depósitos')
        sleep(3)
        os.system('cls')
        return False
    
    else:
        
        depositos = Verdados('depositos','depositos',['dia','hora','Montante','descricao'],f"username = '{username}'")

        if len(depositos) == 0:
            print('Não há movimentos suficientes para extornar')
            sleep(3)
            os.system('cls')
            return False
        
        elif len(depositos) > 0:
            
            while True: 
                for i,deposito in enumerate(depositos):
                    print(f'{i + 1}. {deposito}')
                
                try:
                    opcao = int(input('\nEscolha a operação para extornar (Voltar [0]): '))

                    if opcao >= 0 and opcao <= len(depositos):
                        break

                    else:
                        os.system('cls')
                        print('Opção inválida, tente novamente\n')

                except ValueError:
                    os.system('cls')
                    print('Opção inválida, tente novamente\n')
            
            os.system('cls')
            if opcao == 0:
                return False
            
            else:
                montante = depositos[opcao - 1][2]

                if montante > saldo:
                    print('Não tem fundos suficientes para extornar esta operação')
                    sleep(3)
                    os.system('cls')
                    return False
                
                else:
                    processamento = ''

                    for i in range(100):
                        processamento += '='

                        print(f'{processamento} {i + 1}%')

                        if i < 99:
                            sleep(0.025)
                            os.system('cls')
                        
                        else:
                            dia = depositos[opcao - 1][0]
                            hora = depositos[opcao - 1][1]
                            ApaharLinha('depositos','depositos',f"username = '{username}' AND dia = '{dia}' AND hora = '{hora}'")
                            ActualizarDados('saldo','saldo',f"Montante = '{saldo - montante}'",f"username = '{username}'")
                            print('Processo concluído')
                            sleep(3)
            
            os.system('cls')
            return False