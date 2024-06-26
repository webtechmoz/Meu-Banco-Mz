import sys
import os
from time import sleep

sys.path.append('SQL')

from Dados import Verdados, ActualizarDados, ApaharLinha

def apagarConta(username):

    if username == 'meubancomz50':
        print('Não pode apagar esta conta')
        sleep(3)
        os.system('cls')
        return False
    
    else:
        while True:

            confirmar = input('Deseja apagar a sua conta e todos dados (S/N)?: ').upper()

            if confirmar in ['S','N']:
                break

            else:
                os.system('cls')
                print('Opção inválida, tente novamente\n')
        
        os.system('cls')
        if confirmar == 'N':
            return False
        
        elif confirmar == 'S':
            verSenha = Verdados('usuarios','usuarios',['senha'],f"username = '{username}'")[0][0]

            for i in range(3):
                
                while True:
                    senha = input('Digite a sua senha para confirmar a operação (Voltar [0]): ')

                    if len(senha) <= 5 and senha != '0':
                        os.system('cls')
                        print('Senha inválida, tente novamente!\n')
                    
                    else:
                        break
                
                os.system('cls')
                if senha == '0':
                    return False
                
                elif senha == verSenha:
                    break

                elif senha != verSenha:
                    if i < 2:
                        print(f'A senha digitada está incorrecta. Resta(m) {2 - i} tentativa(s)\n')
                    
                    elif i == 2:
                        os.system('cls')
                        ActualizarDados('usuarios','usuarios',f"bloqueado = 'TRUE'",f"username = '{username}'")
                        print('Excedeu o limite de tentantivas incorrectas. Conta bloqueada')
                        sleep(3)
                        os.system('cls')
                        print('Sessão encerrada com sucesso')
                        exit()
            
            while True:
                confirmar = input('Todos os seus dados serão perdidos e não terá mais acesso à sua conta (S/N)?: ').upper()

                if confirmar in ['S','N']:
                    break

                else:
                    os.system('cls')
                    print('Opção incorrecta, tente novamente!\n')
            
            os.system('cls')
            if confirmar == 'N':
                return False
            
            elif confirmar == 'S':
                processamento = ''
                for i in range(100):
                    processamento += '='

                    print(f'{processamento} {i + 1}%')

                    if i < 99:
                        sleep(0.125)
                        os.system('cls')
                    
                    elif i == 99:
                        # Apagar as informações do usuário

                        ApaharLinha('depositos','depositos',f"username = '{username}'")
                        ApaharLinha('levantamentos','levantamentos',f"username = '{username}'")
                        ApaharLinha('transferencias','transferencias',f"username = '{username}'")
                        ApaharLinha('recebimentos','recebimentos',f"numeroConta = '{username}'")

                        # Desactivar a conta do usuário
                        ActualizarDados('usuarios','usuarios',"bloqueado = 'TRUELY'",f"username = '{username}'")
                        ActualizarDados('saldo','saldo',"Montante = '0'",f"username = '{username}'")
                        print('Processo concluído')
                        sleep(3)
                        os.system('cls')
                        print('Sessão encerrada com êxito')
                        exit()
            
            return False