import pandas as pd
import identificaTabelaCMO
import identificaTabelaEAR
import identificaTabelaHid
import identificaTabelaTer
import identificaTabelaSistema

#IMPORTAR identificaTabelaENA

#monta o dataframe com multiindex:
#as três listas são montadas abaixo e podem ser rearranjadas nos indexes, como for mais conveniente
series = []
for i in range(1,2001):
    series.append(str(i))
variaveis = ['CMO', 'ENA', 'EAR', 'Hid', 'Ter', 'Peq', 'Carga', 'Inter']
meses = ["JAN", "FEV", "MAR", "ABR", "MAI", "JUN", "JUL", "AGO", "SET", "OUT", "NOV", "DEZ", "MEDIA"]

arrays = pd.MultiIndex.from_product([series, meses], names = ['serie', 'mes'])
dfFinal1 = pd.DataFrame(index= arrays, columns= variaveis)
#dfFinal2 = pd.DataFrame(index= arrays,columns= colunas)
#dfFinal3 = pd.DataFrame(index= arrays,columns= colunas)
#dfFinal4 = pd.DataFrame(index= arrays,columns= colunas)

#preencher CMO:
#cmoJan = identificaTabelaCMO.dfCMO1["JAN"]
#print(cmoJan)
#dfFinal1[('CMO')] = identificaTabelaCMO.dfCMO1

print(dfFinal1)