import os
import pandas as pd
import sqlite3 as db

def getCsvPath():
    path_files = []

    for root,dirs,files in os.walk("./microdados_censo_escolar_2020"):
        path = root.split(os.sep)

        for file in files:
            if file.startswith('matricula_') and file.endswith('.CSV'):
                path_files.append(os.path.join(root,file))
    
    return path_files


def createDF(path_list):

    df_final = pd.DataFrame()

    for x in path_list:
        
        df = pd.read_csv(x,sep="|")
        df_final = df_final.append(df)

    return df_final


def sendDfToDb(df_obj):
    conn = db.connect("trybe.db")
    df_obj.to_sql("df_obj", conn, if_exists="replace", chunksize=None,index=False)

    conn.close()


def question_1():
    conn = db.connect("trybe.db")
    df_final = pd.read_sql_query("SELECT CO_MUNICIPIO, count(TP_ETAPA_ENSINO) FROM df_obj WHERE TP_ETAPA_ENSINO==41.0 Group By CO_MUNICIPIO ORDER BY count(TP_ETAPA_ENSINO) DESC LIMIT 10;", conn)
    conn.close()


def question_2():
    conn = db.connect("trybe.db")
    df_final = pd.read_sql_query("SELECT TP_COR_RACA,count(TP_COR_RACA), CO_UF FROM df_obj WHERE TP_COR_RACA != 0 Group By TP_COR_RACA,CO_UF;", conn)
    conn.close()   


if __name__ == '__main__':
    print('Base de dados importada do Censo Escolar do INEP - http://inep.gov.br/microdados')
    
    path = getCsvPath()
    trybe_df = createDF(path)
    
    sendDfToDb(trybe_df)

    print('\n\n########## Quais são os 10 municípios que têm o maior número de pessoas no “Ensino Fundamental de 9 anos - 9º Ano”? ##########\n')
    question_1()
    print('\n########## Qual a distribuição de cores/raças (Branca, Pretas, Pardas, Amarelas e Indígenas) entre os estados ? ##########\n')
    question_2()
    
