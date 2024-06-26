import sys
import os
from time import sleep

sys.path.append('SQL')

from Dados import ActualizarDados, Verdados

def entrar():
    os.system('cls')

    for i in range(3):

        while True:
            username = input('Digite a sua username (Voltar [0]): ').strip()

            if username != '':
                break

            else:
                os.system('cls')
                print('Username inválido, tente novamente!')
                sleep(1)
                os.system('cls')

        if username == '0':
            os.system('cls')
            return False

        while True:
            senha = input('Digite a sua senha (Voltar [0]): ').strip()

            if senha != '':
                break

            else:
                os.system('cls')
                print('Senha inserida é inválida, tente novamente\n')

        
        if senha == '0':
            os.system('cls')
            return False

        try:
            usuario = Verdados('usuarios','usuarios',['nome','username','senha','bloqueado'],f"username = '{username}' AND senha = '{senha}'")
        
        except:
            os.system('cls')
            print('Usuário ou senha inexistente!')
            sleep(2)
            os.system('cls')
            return False

        os.system('cls')
        if len(usuario) > 0:

            if usuario[0][3] == 'FALSE':
                return usuario[0][0], usuario[0][1]
            
            elif usuario[0][3] == 'TRUE':
                print('A sua conta está bloqueada por elevadas tentativas incorrectas')
                sleep(3)
                os.system('cls')
                return False
            
            elif usuario[0][3] == 'TRUELY':
                print('A conta que está a tentar aceder não existe ou está apagada!')
                sleep(3)
                os.system('cls')
                return False
        
        else:
            if i <= 1:
                print(f'Usuário ou senha incorrectos. Resta(m) {2 - i} tentativa(s)\n')
            
            elif i == 2:
                usuario = Verdados('usuarios','usuarios',['nome','username','senha','bloqueado'],f"username = '{username}'")

                if len(usuario) > 0:
                    ActualizarDados('usuarios','usuarios',"bloqueado = 'TRUE'",f"username = '{username}'")
                

                print('A sua conta está bloqueada por elevadas tentativas incorrectas.')
                sleep(3)

                os.system('cls')
                return False