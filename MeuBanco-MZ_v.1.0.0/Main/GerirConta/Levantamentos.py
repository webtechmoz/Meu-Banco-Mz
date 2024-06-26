import sys
import os
from time import sleep

sys.path.append('SQL')
sys.path.append('Auxiliar')

from Dados import InserirDados, ActualizarDados, Verdados
from DatActual import *

def levantamento(username):

    if username == 'meubancomz50':
        os.system('cls')
        print('Não pode efectuar levantamentos nesta conta')
        sleep(3)
        os.system('cls')
        return False
    
    else:
        saldo = Verdados('saldo','saldo',['Montante'],f"username = '{username}'")[0][0]

        if saldo <= 0:
            os.system('cls')
            print('Não tem fundos suficientes para levantar')
            sleep(3)
            os.system('cls')
            return False
        
        else:
        
            while True:
                try:
                    montante = float(input('Digite o valor a levantar (Voltar [0]): '))

                    if saldo >= montante*1.1 or montante == 0:
                        break

                    else:
                        os.system('cls')
                        print('O montante que pretende levantar excede o valor disponível')
                        sleep(3)
                        os.system('cls')
                        return False

                except ValueError:
                    os.system('cls')
                    print('O montante a levantar é inválido!\n')
                
            
            if montante == 0:
                os.system('cls')
                return False
            
            else:
                os.system('cls')
                dia, hora = datactual()
                
                # Actualizar saldo do usuário
                InserirDados('levantamentos','levantamentos',['dia','hora','username','Montante','descricao'],[dia,hora,username,montante,'Levantamento de valores'])
                ActualizarDados('saldo','saldo',f"Montante = '{saldo - montante*1.1}'",f"username = '{username}'")

                # Actualizar comissões
                saldo = Verdados('saldo','saldo',['Montante'],f"username = 'meubancomz50'")[0][0]
                InserirDados('recebimentos','recebimentos',['dia','hora','username','numeroConta','Montante','descricao'],[dia,hora,username,'meubancomz50',montante*0.1,f"Comissões de levantamento de {username}"])
                ActualizarDados('saldo','saldo',f"Montante = '{saldo + montante*0.1}'",f"username = 'meubancomz50'")

                print(f'Levantamento no valor de {round(float(montante),2)} MZN efectuado com sucesso!')
                sleep(3)
                os.system('cls')
            
    return False