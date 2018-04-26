import pandas as pd
pd.set_option('display.width', 400)

tabela = pd.read_fwf('cmarg001.out',
                     sep=' ',
                       delim_whitespace=1)
print(tabela)
print(tabela.iloc[10,0])