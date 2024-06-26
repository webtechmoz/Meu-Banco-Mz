if __name__ != '__main__':
    from Main.GerirConta.GerirMinhaConta.EditarDadosdaConta.EditarNome import *
    from Main.GerirConta.GerirMinhaConta.EditarDadosdaConta.EditarIdade import *
    from Main.GerirConta.GerirMinhaConta.EditarDadosdaConta.EditarSenha import *

else:
    from EditarDadosdaConta.EditarNome import *
    from EditarDadosdaConta.EditarIdade import *
    from EditarDadosdaConta.EditarSenha import *


def editarConta(username):

    while True:
        
        texto = '1 - Editar nome\n2 - Editar idade\n3 - Editar senha\n0 - Voltar'

        opcao = input(f'Escolha uma das opções abaixo\r\n\r\n{texto}: ')

        if opcao in ['0','1','2','3']:
            break

        else:
            os.system('cls')

    os.system('cls')
    if opcao == '0':
        return False
    
    elif opcao == '1':

        editarNome(username)

        return editarConta(username)
    
    elif opcao == '2':

        editarIdade(username)

        return editarConta(username)
    
    elif opcao == '3':

        editarSenha(username)

        return editarConta(username)
    
    return False