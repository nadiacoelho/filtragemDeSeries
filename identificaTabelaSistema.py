import pandas as pd
import numpy as np
pd.set_option('display.width', 400)

#Pequnas:
tabela1 = pd.read_fwf('SISTEMA.DAT',delim_whitespace=1, skiprows= 124)
print(tabela1.head(22))

#monta o dataframe com multiindex:

# arrays = [np.array(['1','1','2','2','3','3','4','4']),
#           np.array('pequenas', 'carga', 'pequenas', 'carga', 'pequenas', 'carga', 'pequenas', 'carga')]
#
# dfSistema = pd.DataFrame(dados, index=arrays)