import pandas as pd
import montaTabelaTotal

#Os dataframes que serão usados no código inteiro. Se definidos como variável global do projeto, essas linhas podem ser suprimidas.
dfSudeste = montaTabelaTotal.dfTotal1
dfSul = montaTabelaTotal.dfTotal2
dfNordeste = montaTabelaTotal.dfTotal3
dfNorte = montaTabelaTotal.dfTotal4

#função que determina o subsistema em questão:
def setSubsistema(n):
    if n == 1:
        return dfSudeste
    elif n == 2:
        return dfSul
    elif n == 3:
        return dfNordeste
    elif n==4:
        return dfNorte

#valores entrados pelo usuário
variavel = 'Ter'
subsistema = 1
valorMax = 3000
m = 'NOV'

#Determinação do filtro:
#para comparar float, é necessario tratar com o valor absoluto
#usar função groupby, método 'filter':

df = setSubsistema(subsistema)
serieFiltro = df.loc[(slice(None), m), variavel] #pd.Series com os valores das series a serem filtrados
filtro = serieFiltro <= valorMax
series = serieFiltro[filtro].index.get_level_values('serie') #séries que atendem a condição

#bools = df.index.get_level_values('serie').isin(series)

#Falta aplicar o filtro do groupby no df com uma das condições:
#  o valor da série estar contido na lista series;
#  o valor do elemento correspondente à serie na lista bools seja True

#df = df.groupby(level = 'serie').filter()
print(df)