import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import os
from carrega_do_banco import importa_sql
from carrega_do_banco import claims

#localizando as pastas
BASE_DIR = os.path.dirname( os.path.dirname( os.path.dirname(  __file__  ) ) )
DATA_DIR = os.path.join( BASE_DIR, 'data' )
SRC_DIR = os.path.join( BASE_DIR, 'src' )
PY_DIR = os.path.join( SRC_DIR, 'python' )
SQL_DIR = os.path.join( SRC_DIR, 'sql' )
PLOT_DIR = os.path.join( BASE_DIR, 'plots' )

#Carregando os dados de claims
#claims = importa_sql(  )

print( claims.head() )

# Data for plotting
t = claims[ "claims" ]
s = claims[ "prob" ]

fig, ax = plt.subplots()
ax.bar(t, s)

ax.set(xlabel='Claim Size', ylabel='Prob.',
       title='Claim Distribution')
ax.grid()

plt.show()

#salvando em svg
fig.savefig( os.path.join ( PLOT_DIR, 'claim_distribution.svg' ), format = 'svg')