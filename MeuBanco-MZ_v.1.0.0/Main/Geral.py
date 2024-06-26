if __name__ != '__main__':
    from Main.GerirConta.Depositos import *
    from Main.GerirConta.Levantamentos import *
    from Main.GerirConta.Transferencias import *
    from Main.GerirConta.Consultar import *
    from Main.GerirConta.MinhaConta import *

else:
    from GerirConta.Depositos import *
    from GerirConta.Levantamentos import *
    from GerirConta.Transferencias import *
    from GerirConta.Consultar import *
    from GerirConta.MinhaConta import *

def geral(nome,username):

    texto = '1 - Depositar\r\n2 - Levantar\r\n3 - Transferir\r\n4 - Consultar\r\n5 - Minha Conta\r\n0 - Sair'

    while True:

        opcao = input(f'Seja Bem-Vindo ao MeuBanco-MZ 3.0\r\n\r\n{texto}: ')

        if opcao in ['0','1','2','3','4','5']:
            break

        else:
            os.system('cls')
            print('Opção selecionada é inválida, tente novamente')
            sleep(3)
            os.system('cls')
    
    if opcao == '0':
        os.system('cls')
        return False
    
    elif opcao == '1':
        os.system('cls')
        deposito(username)
        
        return geral(nome,username)
    
    elif opcao == '2':
        os.system('cls')

        levantamento(username)

        return geral(nome,username)
    
    elif opcao == '3':
        os.system('cls')

        transferir(username)
        
        return geral(nome,username)
    
    elif opcao == '4':
        os.system('cls')

        consulta(username)

        return geral(nome,username)
    
    elif opcao == '5':
        os.system('cls')

        minhaConta(username)

        return geral(nome,username)