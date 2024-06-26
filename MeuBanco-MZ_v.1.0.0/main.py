from Main.CriarUsuario import *
from Main.Entrar import *
from Main.Geral import *
from Main.EsqueciSenha import *
from Main.RecuperarConta import *

def inicio():

    os.system('cls')

    while True:
        opcao = input('1 - Criar Conta\r\n2 - Entrar na Conta\r\n3 - Esqueci a Senha\r\n4 - Recuperar Conta\r\n0 - Sair: ').strip()

        if opcao in ['0','1','2','3','4']:
            break

        else:
            os.system('cls')
            print('Opção inválida, tente novamente\n')

    os.system('cls')
    if opcao == '0':
        return Sair()
    
    elif opcao == '1':
        criarUsuario()
        return inicio()

    elif opcao == '2':
        resposta = entrar()

        if resposta == False:
            return inicio()
        
        elif type(resposta) == tuple:
            conta = geral(resposta[0], resposta[1])

            if conta == False:
                return Sair()
    
    elif opcao == '3':
        recuperarSenha()
        return inicio()
    
    elif opcao == '4':
        recuperarConta()
        return inicio()
    

def Sair():
    print('Saiu com êxito!')


if __name__ == '__main__':
    inicio()