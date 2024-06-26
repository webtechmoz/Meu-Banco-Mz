if __name__ != '__main__':
    from Main.GerirConta.GerirConsultas.ConsultarSaldo import *
    from Main.GerirConta.GerirConsultas.ConsultarMovimentos import *
    from Main.GerirConta.GerirConsultas.ExtractoGeral import *

else:
    from GerirConsultas.ConsultarSaldo import *
    from GerirConsultas.ConsultarMovimentos import *
    from GerirConsultas.ExtractoGeral import *

def consulta(username):

    texto = '1 - Saldo\r\n2 - Movimentos\r\n3 - Extracto Geral\r\n0 - Voltar'

    while True:

        opcao = input(f'Escolha uma das opções abaixo\r\n\r\n{texto}: ').strip()

        os.system('cls')
        if opcao != '':
            break
    
    if opcao == '0':
        return False
    
    elif opcao == '1':
        
        saldo(username)

        return consulta(username)
    
    elif opcao == '2':

        movimentos(username)

        return consulta(username)
    
    elif opcao == '3':

        extractoGeral(username)

        return consulta(username)

    return False