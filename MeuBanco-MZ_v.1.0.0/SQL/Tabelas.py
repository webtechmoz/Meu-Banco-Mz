from Conexao import *

# Criar Tabelas
def CriarTabelas(databasename,tablename,listColumns_and_typeColumns):
    
    database, cursor = ConectarBanco(databasename)
    colunas = ','.join(listColumns_and_typeColumns)

    cursor.execute(f'CREATE TABLE IF NOT EXISTS {tablename} ({colunas})')

    SaveExit(database)


# Apagar Tabela
def ApagarTabela(databasename,tablename):

    database, cursor = ConectarBanco(databasename)

    cursor.execute(f'DROP TABLE {tablename}')
    SaveExit(database)


# Adicionar uma coluna na tabela
def AdicionarColuna(databasename,tablename,listColumns_and_typeColumns):
    
    database, cursor = ConectarBanco(databasename)
    coluna = ','.join(listColumns_and_typeColumns)

    cursor.execute(f'ALTER TABLE {tablename} ADD COLUMN ({coluna})')
    SaveExit(database)


# Apagar uma coluna da tabela
def ApagarColuna(databasename,tablename,columname):

    database, cursor = ConectarBanco(databasename)

    cursor.execute(f'ALTER TABLE {tablename} DROP COLUMN {columname}')
    SaveExit(database)