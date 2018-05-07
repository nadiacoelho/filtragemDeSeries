import pandas as pd
import montaTabelaTotal
import matplotlib.pyplot as plt

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
#função que determina o mês:
def defineMes(mes):
    if mes == 1:
        return 'JAN'
    if mes == 2:
        return 'FEV'
    if mes == 3:
        return 'MAR'
    if mes == 4:
        return 'ABR'
    if mes == 5:
        return 'MAI'
    if mes == 6:
        return 'JUN'
    if mes == 7:
        return 'JUL'
    if mes == 8:
        return 'AGO'
    if mes == 9:
        return 'SET'
    if mes == 10:
        return 'OUT'
    if mes == 11:
        return 'NOV'
    if mes == 12:
        return 'DEZ'

#valores entrados para cada análise:

variavel = 'CMO' #valores possíveis: CMO, ENA, EAR, Hid, Ter, Peq, Carga, Inter
subsistema = 1 #valores possíveis: 1 (SE), 2 (S), 3 (NE), 4 (N)
m = 'AGO'#Mês de referencia para a variável filtrada. Valores possíveis: 'JAN', 'FEV', 'MAR', 'ABR', 'MAI', 'JUN', 'JUL', 'AGO', 'SET', 'OUT', 'NOV', 'DEZ'
comparacao = 3 #valores possíveis: 1 - menor que, 2 - igual a, 3 - maior que
#valores para comparação:
if comparacao == 1:
    valorMax = 0
elif comparacao == 2:
    valor = 0
elif comparacao == 3:
    valorMin = 150

#Determinação do filtro:
df = setSubsistema(subsistema)
serie_a_filtrar = df.loc[(slice(None), m), variavel] #pd.Series com os valores das series a serem filtrados
if comparacao == 1:
    filtro = serie_a_filtrar <= valorMax
elif comparacao == 2:
    filtro = serie_a_filtrar == valor
elif comparacao == 3:
    filtro = serie_a_filtrar >= valorMin

resultFiltro = serie_a_filtrar[filtro].index.get_level_values('serie') #séries que atendem à condição

#Montagem do dataframe final:
dfFiltrado = pd.DataFrame()
for s in resultFiltro:
    aux = df.xs(str(s), level = 'serie')
    aux = pd.concat([aux], keys = [str(s)], names = ['serie'])
    dfFiltrado = dfFiltrado.append(aux)

print(dfFiltrado, '\n')
#plotar graficos:
plt.figure()
dfFiltrado.plot()

print("Numero de series: ", dfFiltrado.index.size/13)