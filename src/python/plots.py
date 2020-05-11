#transformar jupyter para md
#jupyter nbconvert --to md src\python\notebook.ipynb

import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os
from carrega_do_banco import importa_sql
from carrega_do_banco import claims
from carrega_do_banco import all_pagamentos

#localizando as pastas
BASE_DIR = os.path.dirname( os.path.dirname( os.path.dirname(  __file__  ) ) )
DATA_DIR = os.path.join( BASE_DIR, 'data' )
SRC_DIR = os.path.join( BASE_DIR, 'src' )
PY_DIR = os.path.join( SRC_DIR, 'python' )
SQL_DIR = os.path.join( SRC_DIR, 'sql' )
PLOT_DIR = os.path.join( BASE_DIR, 'plots' )

#Carregando os dados de claims
#claims = importa_sql(  )

#print( claims.head() )

# Plot claims
t = claims[ "claims" ]
s = claims[ "prob" ]

fig, ax = plt.subplots()
ax.bar(t, s)

ax.set(xlabel='Claim Size', ylabel='Prob.',
       title='Claim Distribution')
ax.grid()

#plt.show()
#salvando em svg
#fig.savefig( os.path.join ( PLOT_DIR, 'claim_distribution.svg' ), format = 'svg')

all_pagamentos.Pago = all_pagamentos.Pago.astype('int64')

#boxplot por grupo
sns.boxplot( x = 'Año', y = 'Pago', data = all_pagamentos, hue = 'Grupo' )
ax.set(xlabel='Ano', ylabel='Valor',
       title='Boxplot pagamentos por Grupo')
#plt.show()
fig.savefig( os.path.join ( PLOT_DIR, 'boxplot_por_grupo.svg' ), format = 'svg')

#boxplot por tipo
sns.boxplot( x = 'Año', y = 'Pago', data = all_pagamentos, hue = 'Tipo' )
ax.set(xlabel='Ano', ylabel='Valor',
       title='Boxplot pagamentos por Tipo')
#plt.show()
fig.savefig( os.path.join ( PLOT_DIR, 'boxplot_por_tipo.svg' ), format = 'svg')


#boxplot por grupo
for i in [2015, 2016, 2017, 2018]:
    fig, ax = plt.subplots()
    sns.boxplot( x = 'Grupo', y = 'Pago', data = all_pagamentos[ all_pagamentos['Año'] == i ], hue = 'Grupo')
    ax.set(xlabel='Grupo', ylabel='Valor', title='Boxplot pagamentos por Grupo Ano: ' + str(i) )
    #plt.show()
    #fig.savefig( os.path.join ( PLOT_DIR, 'boxplot_por_grupo' + str(i) + '.svg' ), format = 'svg')

    print(all_pagamentos[ all_pagamentos['Año'] == i ].Grupo.unique())


#boxplot por tipo
for i in [2015, 2016, 2017, 2018]:
    fig, ax = plt.subplots()
    sns.boxplot( x = 'Tipo', y = 'Pago', data = all_pagamentos[ all_pagamentos['Año'] == i ], hue = 'Tipo')
    ax.set(xlabel='Tipo', ylabel='Valor', title='Boxplot pagamentos por Tipo Ano: ' + str(i) )
    plt.show()
    #fig.savefig( os.path.join ( PLOT_DIR, 'boxplot_por_tipo' + str(i) + '.svg' ), format = 'svg')

    print(all_pagamentos[ all_pagamentos['Año'] == i ].Tipo.unique())