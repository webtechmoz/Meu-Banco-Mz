if __name__ != '__main__':
    from Main.GerirConta.GerirMinhaConta.DadosdaConta import *
    from Main.GerirConta.GerirMinhaConta.EditarConta import *
    from Main.GerirConta.GerirMinhaConta.ExtornarOperacao import *
    from Main.GerirConta.GerirMinhaConta.ApagarConta import *

else:
    from GerirMinhaConta.DadosdaConta import *
    from GerirMinhaConta.EditarConta import *
    from GerirMinhaConta.ExtornarOperacao import *
    from GerirMinhaConta.ApagarConta import *


def minhaConta(username):

    while True:
        texto = '1 - Dados da Conta\r\n2 - Editar Dados da Conta\r\n3 - Extornar Operação\r\n4 - Apagar a Conta\r\n0 - Voltar'

        opcao = input(f'Escolha uma das opções abaixo\r\n\r\n{texto}: ').strip()

        if opcao in ['0','1','2','3','4']:
            break

        else:
            os.system('cls')
        
    
    os.system('cls')
    if opcao == '0':
        return False
    
    elif opcao == '1':

        dadosdaConta(username)

        return minhaConta(username)
    
    elif opcao == '2':

        editarConta(username)

        return minhaConta(username)
    
    elif opcao == '3':

        extornarOperacoes(username)

        return minhaConta(username)
    
    elif opcao == '4':

        apagarConta(username)

        return minhaConta(username)
    
    return False