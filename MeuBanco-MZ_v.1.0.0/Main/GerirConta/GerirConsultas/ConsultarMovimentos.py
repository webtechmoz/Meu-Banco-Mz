if __name__ != '__main__':
    from Main.GerirConta.GerirConsultas.GerirMovimentos.ConsultarDepositos import *
    from Main.GerirConta.GerirConsultas.GerirMovimentos.ConsultarLevantamentos import *
    from Main.GerirConta.GerirConsultas.GerirMovimentos.ConsultarTransferencias import *
    from Main.GerirConta.GerirConsultas.GerirMovimentos.ConusltarRecebimentos import *

else:
    from GerirMovimentos.ConsultarDepositos import *
    from GerirMovimentos.ConsultarLevantamentos import *
    from GerirMovimentos.ConsultarTransferencias import *
    from GerirMovimentos.ConusltarRecebimentos import *


def movimentos(username):

    texto = '1 - Depósitos\r\n2 - Levantamentos\r\n3 - Transferências\r\n4 - Recebimentos\r\n0 - Voltar'

    while True:

        opcao = input(f'Escolha uma das opções abaixo\r\n\r\n{texto}: ').strip()

        os.system('cls')
        if opcao != '':
            break
    
    if opcao == '0':
        return False
    
    elif opcao == '1':
        
        Depositos(username)

        return movimentos(username)

    elif opcao == '2':

        Levantamentos(username)

        return movimentos(username)
    
    elif opcao == '3':

        Transferencias(username)

        return movimentos(username)
    
    elif opcao == '4':
        
        Recebimentos(username)

        return movimentos(username)