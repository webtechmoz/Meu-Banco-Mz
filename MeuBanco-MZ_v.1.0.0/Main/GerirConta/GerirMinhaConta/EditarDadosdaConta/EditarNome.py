import sys
import os
from time import sleep

sys.path.append('SQL')
sys.path.append('Auxiliar')

from Dados import ActualizarDados, Verdados
from ProcurarEspaco import *

def editarNome(username):

    while True:

        nome = Verdados('usuarios','usuarios',['nome'],f"username = '{username}'")[0][0]

        opcao = input(f'O seu nome actual é {nome}, deseja editar (S/N)?: ').upper()

        if opcao in ['S','N']:
            break

        else:
            print('Opção inválida, tente novamente\n')
            os.system('cls')
    
    os.system('cls')
    if opcao == 'N':
        return False
    
    
    elif opcao == 'S':

        while True:
            novoNome = input('Digite o seu novo nome completo (Voltar [0]): ').strip()

            if (len(novoNome) > 5 and procurarEspaco(novoNome) == True) or novoNome == '0':
                break

            else:
                os.system('cls')
                print('Nome inválido, tente novamente\n')
        
        os.system('cls')
        if novoNome == '0':
            os.system('cls')
            return False
        
        else:
            if novoNome == nome:
                print('Operação cancelada, o novo nome é igual ao anterior')
                sleep(3)
                os.system('cls')
                return False
            
            else:
                processamento = ''
                for i in range(100):
                    processamento += '='

                    print(f'{processamento} {i + 1}%')

                    if i < 99:
                        sleep(0.08)
                        os.system('cls')
                    
                    else:
                        ActualizarDados('usuarios','usuarios',f"nome = '{novoNome}'",f"username = '{username}'")
                        print('Processo concluído')
                        sleep(3)
                
                os.system('cls')
                return False