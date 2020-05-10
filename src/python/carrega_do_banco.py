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
str_connection = 'sqlite:///' + os.path.join( DATA_DIR, 'itam_ih.db' )
engine = sqlalchemy.create_engine( str_connection )
connection = engine.connect()

#importa query
with open( os.path.join(SQL_DIR, 'soma_sinistro_anual_per_group.sql') ) as query_file:
    query = query_file.read()

#anual_tipo = pd.read_sql_query(query, connection)
#anual_tipo.head()

