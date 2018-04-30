import pandas as pd
pd.set_option('display.width', 400)

#importação do arquivo considerando o ano 2018(o ano vigente), que no arquivo vai até a linha 2000 (2000 series)
tabela1 = pd.read_fwf('earmfpm001.out',delim_whitespace=1, skiprows= 2)
tabela1_2018 = tabela1.iloc[:2000,:]
tabela2 = pd.read_fwf('earmfpm002.out',delim_whitespace=1, skiprows= 2)
tabela2_2018 = tabela2.iloc[:2000,:]
tabela3 = pd.read_fwf('earmfpm003.out',delim_whitespace=1, skiprows= 2)
tabela3_2018 = tabela3.iloc[:2000,:]
tabela4 = pd.read_fwf('earmfpm004.out',delim_whitespace=1, skiprows= 2)
tabela4_2018 = tabela4.iloc[:2000,:]

#ajuste dos dataframes:
dfEAR1 = tabela1_2018.transpose()
dfEAR1.insert(loc = 0, column = 'index', value = ['SERIE','JAN', 'FEV', 'MAR', 'ABR', 'MAI', 'JUN', 'JUL', 'AGO', 'SET', 'OUT', 'NOV', 'DEZ', 'MEDIA'])
dfEAR1 = dfEAR1.set_index('index')
dfEAR1 = dfEAR1.transpose()
dfEAR1.pop("SERIE")

dfEAR2 = tabela2_2018.transpose()
dfEAR2.insert(loc = 0, column = 'index', value = ['SERIE','JAN', 'FEV', 'MAR', 'ABR', 'MAI', 'JUN', 'JUL', 'AGO', 'SET', 'OUT', 'NOV', 'DEZ', 'MEDIA'])
dfEAR2 = dfEAR2.set_index('index')
dfEAR2 = dfEAR2.transpose()
dfEAR2.pop("SERIE")

dfEAR3 = tabela3_2018.transpose()
dfEAR3.insert(loc = 0, column = 'index', value = ['SERIE','JAN', 'FEV', 'MAR', 'ABR', 'MAI', 'JUN', 'JUL', 'AGO', 'SET', 'OUT', 'NOV', 'DEZ', 'MEDIA'])
dfEAR3 = dfEAR3.set_index('index')
dfEAR3 = dfEAR3.transpose()
dfEAR3.pop("SERIE")

dfEAR4 = tabela4_2018.transpose()
dfEAR4.insert(loc = 0, column = 'index', value = ['SERIE','JAN', 'FEV', 'MAR', 'ABR', 'MAI', 'JUN', 'JUL', 'AGO', 'SET', 'OUT', 'NOV', 'DEZ', 'MEDIA'])
dfEAR4 = dfEAR4.set_index('index')
dfEAR4 = dfEAR4.transpose()
dfEAR4.pop("SERIE")