from Conexao import *

# Inserir valores na Tabela
def InserirDados(databasename,tablename,listColumns,listValues):

    database, cursor = ConectarBanco(databasename)
    colunas = ','.join(listColumns)

    listaValores = []
    for i in range(len(listValues)):
        if type(listValues[i]) == str:
            listaValores.append(f"'{listValues[i]}'")
        else:
            listaValores.append(f"{listValues[i]}")
    
    valores = ','.join(listaValores)

    cursor.execute(f'INSERT INTO {tablename} ({colunas}) VALUES ({valores})')
    SaveExit(database)


# Apagar uma linha na tabela
def ApaharLinha(databasename,tablename,conditions):
    
    database, cursor = ConectarBanco(databasename)
    
    cursor.execute(f'DELETE FROM {tablename} WHERE {conditions}')
    SaveExit(database)

# Actualizar registo na tabela
def ActualizarDados(databasename,tablename,column_and_value,index = ''):
    
    database, cursor = ConectarBanco(databasename)
    
    if index != '':
        cursor.execute(f'UPDATE {tablename} SET {column_and_value} WHERE {index}')
    
    else:
        cursor.execute(f'UPDATE {tablename} SET {column_and_value}')
    
    SaveExit(database)


# Ver dados na base de dados
def Verdados(databasename,tablename,listColumns,conditions=''):

    database, cursor = ConectarBanco(databasename)
    colunas = ','.join(listColumns)

    if conditions == '':
        cursor.execute(f'SELECT {colunas} FROM {tablename}')
    
    else:
        cursor.execute(f'SELECT {colunas} FROM {tablename} WHERE {conditions}')
        
    dados = cursor.fetchall()
    SaveExit(database)
    
    return dados