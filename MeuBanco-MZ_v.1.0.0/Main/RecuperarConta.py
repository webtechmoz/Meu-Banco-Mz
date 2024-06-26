import sys
import os
from time import sleep

sys.path.append('SQL')

from Dados import ActualizarDados, Verdados

def recuperarConta():

    for i in range(3):
        
        while True:
            os.system('cls')
            username = input('Digite o seu número de conta (Voltar [0]): ').strip()

            if username != '':
                break

            else:
                os.system('cls')
                print('Número de Conta inválido, tente novamente!')
                sleep(3)
                os.system('cls')
        
        if username == '0':
            os.system('cls')
            return False

        try:
            usuario = Verdados('usuarios','usuarios',['nome','username','idade','bloqueado'],f"username = '{username}'")

        except:
            os.system('cls')
            print('Este usuário não pode ser recuperado, contacte o administrador!')
            sleep(3)
            break

        if len(usuario) > 0:

            if usuario[0][3] != 'TRUELY':
                os.system('cls')
                print('Este usuário não pode ser recuperado, contacte o administrador!')
                sleep(3)
                os.system('cls')
                return False
            
            else:
                while True:
                    os.system('cls')
                    nome = input('Digite o seu nome (Voltar [0]): ').strip()

                    if nome != '':
                        break

                    else:
                        os.system('cls')
                        print('O nome é inválido, tente novamente!')
                        sleep(3)
                        os.system('cls')
                
                os.system('cls')
                if nome == '0':
                    return False
                
                while True:
                    try:
                        idade = int(input('Digite a sua idade (Voltar [0]): ').strip())

                        break

                    except ValueError:
                        os.system('cls')
                        print('Valor inserido é inválido, tente novamente!')
                        sleep(3)
                        os.system('cls')
                
                os.system('cls')
                if idade == 0:
                    return False
                

                while True:
                    while True:
                        senha = input('Digite a sua nova senha (Voltar [0]): ').strip()

                        if (len(senha) > 5 and senha != username) or senha == '0':
                            break

                        else:
                            os.system('cls')
                            print('Senha inserida é inválida, tente novamente\n')
                    
                    if senha == '0':
                        os.system('cls')
                        return False
                    
                    os.system('cls')
                    confirmarSenha = input('Confirme a sua nova senha (Voltar [0]): ').strip()

                    if confirmarSenha == senha or confirmarSenha == '0':
                        break

                    else:
                        os.system('cls')
                        print('As senhas não correspondem, tente novamente\n')
                
                if confirmarSenha == '0':
                    os.system('cls')
                    return False
                
                os.system('cls')

                # Actualizando os dados na base de dados de usuários
                processamento = ''
                for i in range(100):
                    processamento += '='

                    print(f'{processamento} {i + 1}%')
                    
                    if i < 99:
                        sleep(0.125)
                        os.system('cls')
                        
                    if i == 99:
                        ActualizarDados('usuarios','usuarios',f"nome = '{nome}'",f"username = '{username}'")
                        ActualizarDados('usuarios','usuarios',f"senha = '{idade}'",f"username = '{username}'")
                        ActualizarDados('usuarios','usuarios',f"senha = '{senha}'",f"username = '{username}'")
                        ActualizarDados('usuarios','usuarios',"bloqueado = 'FALSE'",f"username = '{username}'")

                        print('Conta recuperada com sucesso')
                        sleep(3)
                    
                
                os.system('cls')
                return False
        
        else:
            if i <= 1:
                os.system('cls')
                print(f'A conta que está a tentar recuperar não existe ou foi apagada. Resta (m) {2 - i} tentativa (s)')
                sleep(3)
                os.system('cls')
            
            else:
                os.system('cls')
                print('Excedeu o limite de tentativas incorrectas!')
                sleep(3)
    
    os.system('cls')
    return False