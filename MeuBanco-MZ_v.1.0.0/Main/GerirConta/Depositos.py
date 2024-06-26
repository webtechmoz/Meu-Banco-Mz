import sys
import os
from time import sleep

sys.path.append('SQL')
sys.path.append('Auxiliar')

from Dados import InserirDados, ActualizarDados, Verdados
from DatActual import *

def deposito(username):
    
    if username == 'meubancomz50':
        os.system('cls')
        print('Não pode efectuar depósitos nesta conta')
        sleep(3)
        os.system('cls')
        return False
    
    else:
        while True:
            try:
                montante = float(input('Digite o valor a depositar (Voltar [0]): '))

                break

            except ValueError:
                os.system('cls')
                print('O montante a depositar é inválido!\n')
            
        
        if montante == 0:
            os.system('cls')
            return False
        
        else:
            os.system('cls')
            saldo = Verdados('saldo','saldo',['Montante'],f"username = '{username}'")[0][0]
            dia, hora = datactual()

            InserirDados('depositos','depositos',['dia','hora','username','Montante','descricao'],[dia,hora,username,montante,'Depósito de valores'])
            ActualizarDados('saldo','saldo',f"Montante = '{saldo + montante}'",f"username = '{username}'")

            print(f'Depósito no valor de {round(float(montante),2)} MZN efectuado com sucesso!')
            sleep(3)
            os.system('cls')
            
    return False