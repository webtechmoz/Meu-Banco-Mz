if __name__ != '__main__':
    from Main.GerirConta.GerirMinhaConta.GerirExtornos.ExtornarDepositos import *
    from Main.GerirConta.GerirMinhaConta.GerirExtornos.ExtornarTransferencias import *

else:
    from GerirExtornos.ExtornarDepositos import *
    from GerirExtornos.ExtornarTransferencias import *


def extornarOperacoes(username):

    texto = '1 - Depósitos\r\n2 - Transferências\r\n0 - Voltar: '

    while True:

        opcao = input(f'Escolha uma das opções abaixo\r\n\r\n{texto}: ').strip()

        if opcao != '':
            break
    
    os.system('cls')
    if opcao == '0':
        return False
    
    elif opcao == '1':

        extornarDepositos(username)

        return extornarOperacoes(username)
    
    elif opcao == '2':

        extornarTransferencias(username)

        return extornarOperacoes(username)