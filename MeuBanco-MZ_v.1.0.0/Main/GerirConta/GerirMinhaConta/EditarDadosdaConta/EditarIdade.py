import sys
import os
from time import sleep

sys.path.append('SQL')

from Dados import ActualizarDados, Verdados

def editarIdade(username):

    idade = Verdados('usuarios','usuarios',['idade'],f"username = '{username}'")[0][0]

    while True:

        opcao = input(f'A sua idade actual é de {idade} anos, deseja editar (S/N)?: ').upper()

        if opcao in ['S','N']:
            break

        else:
            print('Opção inválida, tente novamente\n')
            os.system('cls')
    
    os.system('cls')
    if opcao == 'N':
        return False
    
    else:
        while True:
            try:
                novaIdade = int(input('Digite a sua nova idade (Voltar [0]): ').strip())

                if novaIdade > 15 or novaIdade == 0:
                    break

                else:
                    os.system('cls')
                    print('Valor inserido está invalido, tente novamente\n')
            
            except:
                os.system('cls')
                print('Valor inserido é inválido, tente novamente!\n')

        os.system('cls')
        if novaIdade == 0:
            return False
        
        else:
            if novaIdade == idade:
                print('Operação cancelada, a sua nova idade não pode ser igual a anterior')
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
                    
                    elif i == 99:
                        ActualizarDados('usuarios','usuarios',f"idade = '{novaIdade}'",f"username = '{username}'")
                        print('Processo concluído')
                        sleep(3)
        
        os.system('cls')
        return False