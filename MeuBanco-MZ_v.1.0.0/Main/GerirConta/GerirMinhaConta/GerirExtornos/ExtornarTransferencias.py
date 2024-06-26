import sys
import os
from time import sleep

sys.path.append('SQL')

from Dados import Verdados, ApaharLinha, ActualizarDados

def extornarTransferencias(username):

    saldo = Verdados('saldo','saldo',['Montante'],f"username = '{username}'")[0][0]
    
    transferencias = Verdados('transferencias','transferencias',['dia','hora','numeroConta','Montante','descricao'],f"username = '{username}'")

    if len(transferencias) == 0:
        print('Não há movimentos suficientes para extornar')
        sleep(3)
        os.system('cls')
        return False
    
    elif len(transferencias) > 0:
        
        while True: 
            for i,transferencia in enumerate(transferencias):
                print(f'{i + 1}. {transferencia}')
            
            try:
                opcao = int(input('\nEscolha a operação para extornar (Voltar [0]): '))

                if opcao >= 0 and opcao <= len(transferencias):
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
            montante = transferencias[opcao - 1][3]

            processamento = ''

            for i in range(100):
                processamento += '='

                print(f'{processamento} {i + 1}%')

                if i < 99:
                    sleep(0.025)
                    os.system('cls')
                
                else:
                    dia = transferencias[opcao - 1][0]
                    hora = transferencias[opcao - 1][1]
                    numeroConta = transferencias[opcao - 1][2]

                    # Actualizar os movimentos do usuário
                    ApaharLinha('transferencias','transferencias',f"username = '{username}' AND dia = '{dia}' AND hora = '{hora}'")
                    ActualizarDados('saldo','saldo',f"Montante = '{saldo + montante*1.1}'",f"username = '{username}'")

                    # Actualizar os movimentos do beneficiário
                    saldo = Verdados('saldo','saldo',['Montante'],f"username = '{numeroConta}'")[0][0]
                    ApaharLinha('recebimentos','recebimentos',f"numeroConta = '{numeroConta}' AND dia = '{dia}' AND hora = '{hora}'")
                    ActualizarDados('saldo','saldo',f"Montante = '{saldo - montante}'",f"username = '{numeroConta}'")

                    # Actualizar os movimentos das comissões
                    saldo = Verdados('saldo','saldo',['Montante'],f"username = 'meubancomz50'")[0][0]
                    ApaharLinha('recebimentos','recebimentos',f"numeroConta = 'meubancomz50' AND dia = '{dia}' AND hora = '{hora}'")
                    ActualizarDados('saldo','saldo',f"Montante = '{saldo - montante*0.1}'",f"username = 'meubancomz50'")
                    print('Processo concluído')
                    sleep(3)
        
        os.system('cls')
        return False