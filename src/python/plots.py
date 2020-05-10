import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import os

#localizando as pastas
BASE_DIR = os.path.dirname( os.path.dirname( os.path.dirname(  __file__  ) ) )
DATA_DIR = os.path.join( BASE_DIR, 'data' )
SRC_DIR = os.path.join( BASE_DIR, 'src' )
PY_DIR = os.path.join( SRC_DIR, 'python' )
SQL_DIR = os.path.join( SRC_DIR, 'sql' )
PLOT_DIR = os.path.join( BASE_DIR, 'plots' )

# Data for plotting
t = np.arange(0.0, 2.0, 0.01)
s = 1 + np.sin(2 * np.pi * t)

fig, ax = plt.subplots()
ax.plot(t, s)

ax.set(xlabel='time (s)', ylabel='voltage (mV)',
       title='About as simple as it gets, folks')
ax.grid()

#salvando em svg
fig.savefig( os.path.join ( PLOT_DIR, 'teste2.svg' ), format = 'svg')