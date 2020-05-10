import os
import sqlalchemy
import pandas as pd
import numpy as np

#localizando as pastas
BASE_DIR = os.path.dirname( os.path.dirname( os.path.dirname(  __file__  ) ) )
DATA_DIR = os.path.join( BASE_DIR, 'data' )
SRC_DIR = os.path.join( BASE_DIR, 'src' )
PY_DIR = os.path.join( SRC_DIR, 'python' )
SQL_DIR = os.path.join( SRC_DIR, 'sql' )

#conexão
str_connection = os.path.join( 'sqlite:///', DATA_DIR, 'itam_ih.db' )
engine = sqlalchemy.create_engine( str_connection )
connection = engine.connect()

# Encontrando os arquivos de dados
files_names = [ i for i in os.listdir( DATA_DIR ) if i.endswith('.csv') ]

def data_quality(x):
    if type(x) == str:
        return x.replace(",", "").replace("$", '')
    else:
        return x

for i in files_names:
    df = pd.read_csv( os.path.join( DATA_DIR, i ) )

    for c in df.columns:
        df[c] = df[c].apply(data_quality)

    table_names = i.strip( '*.csv' ).replace( " ", '_' )
    print(table_names)

    df.to_sql(  table_names,
                connection,
                if_exists= 'replace' )

df = pd.read_csv( os.path.join( DATA_DIR, files_names[0] ) )
