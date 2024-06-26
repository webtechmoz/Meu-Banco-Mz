import sys
import os
from time import sleep

sys.path.append('Auxiliar')
sys.path.append('SQL')

from ProcurarEspaco import procurarEspaco
from Tabelas import CriarTabelas
from Dados import InserirDados, Verdados

def criarUsuario():

    # Criar Bases de Dados
    try:
        CriarTabelas('usuarios','usuarios',['id INTEGER PRIMARY KEY AUTOINCREMENT','nome TEXT', 'idade INTEGER', 'username TEXT','senha TEXT','bloqueado TEXT'])
        CriarTabelas('saldo','saldo',['id INTEGER PRIMARY KEY','username TEXT', 'Montante NUMERIC'])
        CriarTabelas('transferencias','transferencias',['id INTEGER PRIMARY KEY AUTOINCREMENT','dia TEXT','hora TEXT','username TEXT','numeroConta TEXT','Montante NUMERIC','descricao TEXT'])
        CriarTabelas('recebimentos','recebimentos',['id INTEGER PRIMARY KEY AUTOINCREMENT','dia TEXT','hora TEXT','username TEXT','numeroConta TEXT','Montante NUMERIC','descricao TEXT'])
        CriarTabelas('depositos','depositos',['id INTEGER PRIMARY KEY AUTOINCREMENT','dia TEXT','hora TEXT','username TEXT','Montante NUMERIC','descricao TEXT'])
        CriarTabelas('levantamentos','levantamentos',['id INTEGER PRIMARY KEY AUTOINCREMENT','dia TEXT','hora TEXT','username TEXT','Montante NUMERIC','descricao TEXT'])

    except:
        os.system('cls')
        print('Ocorreu um erro ao importar as bases de dados.')
        sleep(3)
        return False

    while True:
        nome = input('Digite o seu nome completo (Voltar [0]): ').strip()

        if (len(nome) > 5 and procurarEspaco(nome) == True) or nome == '0':
            break

        else:
            os.system('cls')
            print('Nome inválido, tente novamente\n')
    
    if nome == '0':
        os.system('cls')
        return False
    
    os.system('cls')
    while True:
        try:
            idade = int(input('Digite a sua idade (Voltar [0]): ').strip())

            if idade > 15 or idade == 0:
                break

            else:
                os.system('cls')
                print('Valor inserido está invalido, tente novamente\n')
        
        except:
            os.system('cls')
            print('Valor inserido é inválido, tente novamente!\n')
    
    if idade == 0:
        os.system('cls')
        return False
    
    os.system('cls')
    while True:

        username = input('Digite a sua username (Voltar [0]): ').strip()

        verificarUser = Verdados('usuarios','usuarios',['username'],f"username = '{username}'")

        if len(verificarUser) > 0:
            os.system('cls')
            print(f'{username}, já está sendo usado por outro cliente')
            sleep(2)
            os.system('cls')

        elif len(username) > 4 or username == '0':
            break

        else:
            os.system('cls')
            print('Valor inserido está inválido, tente novamente\n')
    
    if username == '0':
        os.system('cls')
        return False
    
    os.system('cls')
    while True:
        while True:
            senha = input('Digite a sua senha (Voltar [0]): ').strip()

            if (len(senha) > 5 and senha != username) or senha == '0':
                break

            else:
                os.system('cls')
                print('Senha inserida é inválida, tente novamente\n')
        
        if senha == '0':
            os.system('cls')
            return False
        
        os.system('cls')
        confirmarSenha = input('Confirme a sua senha (Voltar [0]): ').strip()

        if confirmarSenha == senha or confirmarSenha == '0':
            break

        else:
            os.system('cls')
            print('As senhas não correspondem, tente novamente\n')
    
    if confirmarSenha == '0':
        os.system('cls')
        return False
    
    os.system('cls')
    
    # Criando o usuário na base de dados
    processamento = ''
    for i in range(100):
        processamento += '='

        print(f'{processamento} {i + 1}%')
        sleep(0.125)

        if i == 99:
            InserirDados('usuarios','usuarios',['nome','idade','username','senha','bloqueado'],[nome,idade,username,senha,'FALSE'])
            InserirDados('saldo','saldo',['username','Montante'],[username,0])
            print(f'O cliente {nome} foi criado com sucesso!')
            sleep(3)
        
        os.system('cls')
        
    return False