import sys
import os
from time import sleep

sys.path.append('SQL')

from Dados import ActualizarDados, Verdados

def editarSenha(username):

    senha = Verdados('usuarios','usuarios',['senha'],f"username = '{username}'")[0][0]

    while True:
        opcao = input('Deseja mesmo alterar a sua senha (S/N)?: ').upper()

        if opcao in ['S','N']:
            break

        else:
            os.system('cls')
            print('Opção inválida, tente novamente\n')


    os.system('cls')

    if opcao == 'S':
        for i in range(3):
            
            while True:
                verSenha = input('Digite a sua senha actual (Voltar [0]): ').strip()

                if verSenha != '':
                    break
                
                else:
                    os.system('cls')
                    print('Senha inválida, tente novamente!\n')
            
            os.system('cls')
            if verSenha == '0':
                return False
            
            elif verSenha == senha:

                while True:
                    while True:
                        novaSenha = input('Digite a sua senha (Voltar [0]): ').strip()

                        if (len(novaSenha) > 5 and novaSenha != username) or novaSenha == '0':
                            break

                        else:
                            os.system('cls')
                            print('Senha inserida é inválida, tente novamente\n')
                    
                    if novaSenha == '0':
                        os.system('cls')
                        return False
                    
                    elif novaSenha == senha:
                        os.system('cls')
                        print('Operação cancelada, a nova senha deve ser diferente da actual')
                        sleep(3)
                        os.system('cls')
                        return False
                    
                    os.system('cls')
                    confirmarSenha = input('Confirme a sua senha (Voltar [0]): ').strip()

                    if confirmarSenha == novaSenha or confirmarSenha == '0':
                        break

                    else:
                        os.system('cls')
                        print('As senhas não correspondem, tente novamente\n')
                
                if confirmarSenha == '0':
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
                            ActualizarDados('usuarios','usuarios',f"senha = '{novaSenha}'",f"username = '{username}'")
                            print('Operação concluída')
                            sleep(3)
                            os.system('cls')
                            return False
            
            elif verSenha != senha:
                if i < 2:
                    os.system('cls')
                    print(f'A senha inserida está incorrecta. Resta(m) {2 - i} tentantiva(s)\n')
                
                elif i == 2:
                    os.system('cls')
                    ActualizarDados('usuarios','usuarios',f"bloqueado = 'TRUE'",f"username = '{username}'")
                    print('Excedeu o limite de tentantivas incorrectas. Conta bloqueada')
                    sleep(3)
                    os.system('cls')
                    print('Sessão encerrada com sucesso')
                    exit()
    
    else:
        return False