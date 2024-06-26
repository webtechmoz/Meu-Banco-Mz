import sys
import os
from time import sleep

sys.path.append('SQL')
sys.path.append('Auxiliar')

from Dados import InserirDados, ActualizarDados, Verdados
from DatActual import *

def transferir(username):
    
    if username == 'meubancomz50':
        os.system('cls')
        print('Não pode efectuar transferêcias com esta conta!')
        sleep(3)
        os.system('cls')
        return False
    
    else:
        saldo = Verdados('saldo','saldo',['Montante'],f"username = '{username}'")[0][0]

        if saldo <= 0:
            os.system('cls')
            print('Não tem fundos disponíveis para transferir')
            sleep(3)
            os.system('cls')
            return False
        
        else:
            while True:

                numeroConta = input('Digite o número da conta (Voltar [0]): ').strip()

                if numeroConta != '':
                    break
            
            os.system('cls')
            if numeroConta == '0':
                return False
            
            elif numeroConta == 'meubancomz50':
                print('Esta número de conta não pode receber transferência')
                sleep(3)
                os.system('cls')
                return False

            elif numeroConta == username:
                print('Não pode efectuar transferências para si próprio')
                sleep(3)
                os.system('cls')
                return False
            
            else:
                verConta = Verdados('usuarios','usuarios',['username','bloqueado'],f"username = '{numeroConta}'")

                if len(verConta) == 0:
                    print('O número de conta inserido não existe!')
                    sleep(3)
                    os.system('cls')
                    return False
                
                else:
                    if verConta[0][1] == 'TRUELY':
                        print('O número de conta inserido já não existe na nossa base de dados')
                        sleep(3)
                        os.system('cls')
                        return False
                    
                    while True:
                        try:
                            montante = float(input('Digite o valor a transferir (Voltar [0]): '))

                            break

                        except ValueError:
                            os.system('cls')
                            print('O montante inserido é inválido, tente novamente\n')
                    
                    os.system('cls')
                    if montante == 0:
                        os.system('cls')
                        return False
                    
                    else:

                        if saldo < montante*1.1:
                            print('O valor a transferir excede os fundos disponíveis')
                            sleep(3)
                            os.system('cls')
                            return False
                        
                        else:
                            dia, hora = datactual()

                            # Actualizar saldo do cliente
                            InserirDados('transferencias','transferencias',['dia','hora','username','numeroConta','Montante','descricao'],[dia,hora,username,numeroConta,montante,f'Transferência de valores para {numeroConta}'])
                            ActualizarDados('saldo','saldo',f"Montante = '{saldo - montante*1.1}'",f"username = '{username}'")

                            # Actualizar saldo do beneficiário
                            saldo = Verdados('saldo','saldo',['Montante'],f"username = '{numeroConta}'")[0][0]
                            InserirDados('recebimentos','recebimentos',['dia','hora','username','numeroConta','Montante','descricao'],[dia,hora,username,numeroConta,montante,f'Recebimento de valores de {username}'])
                            ActualizarDados('saldo','saldo',f"Montante = '{saldo + montante}'",f"username = '{numeroConta}'")

                            # Actualizar o valor das comissões do banco
                            saldo = Verdados('saldo','saldo',['Montante'],f"username = 'meubancomz50'")[0][0]
                            InserirDados('recebimentos','recebimentos',['dia','hora','username','numeroConta','Montante','descricao'],[dia,hora,username,'meubancomz50',montante*0.1,f'Comissões de transferência de {username}'])
                            ActualizarDados('saldo','saldo',f"Montante = '{saldo + montante*0.1}'",f"username = 'meubancomz50'")

                            print(f'Transferência no valor de {round(montante,2)} MZN para {numeroConta} feito com sucesso')
                            sleep(3)
                            os.system('cls')

        return False