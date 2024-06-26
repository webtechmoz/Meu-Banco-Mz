import sqlite3 as sq
from pathlib import Path

# Criar Banco de Dados
def ConectarBanco(databasename: str):
    path =Path.cwd() / 'SQL/DadosSQL'
    path.mkdir(parents=True, exist_ok= True)
    database = sq.connect(fr'{path}\{databasename}.db')
    cursor = database.cursor()
    
    return database, cursor


# Salvar alterações e guardar
def SaveExit(database: sq.Connection):
    database.commit()
    database.close()