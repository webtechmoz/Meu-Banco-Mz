import sys
import os

sys.path.append('SQL')
sys.path.append('Auxiliar')

from Dados import Verdados
from DatActual import *

def saldo(username):
    
    while True:
        dia, hora = datactual()
        saldo = Verdados('saldo','saldo',['username','Montante'],f"username = '{username}'")[0]

        opcao = input(f'Dia: {dia}\r\nHora: {hora}\r\nSaldo: {round(float(saldo[1]),2)} MZN\r\nNúmero da Conta: {saldo[0]}\r\n\r\nVoltar [0]: ')

        os.system('cls')
        if opcao == '0':
            break

    return False