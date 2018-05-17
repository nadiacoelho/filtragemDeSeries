import pandas as pd
writer1 = pd.ExcelWriter('AnaliseNewave.xlsx', engine= 'openpyxl')
writer2 = pd.ExcelWriter('DebugFiltro.xlsx', engine= 'openpyxl')
pd.set_option('display.width', 500)

#Os dataframes que serão usados no código inteiro. Se definidos como variável global do projeto, essas linhas podem ser suprimidas.
dfSudeste = pd.read_csv('Tabela1').set_index(['serie', 'mes']).fillna(0)
dfSul = pd.read_csv('Tabela2').set_index(['serie', 'mes']).fillna(0)
dfNordeste = pd.read_csv('Tabela3').set_index(['serie', 'mes']).fillna(0)
dfNorte = pd.read_csv('Tabela4').set_index(['serie', 'mes']).fillna(0)

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
    if mes == 13:
        return 'MEDIA'

#df=setSubsistema(1)
#print("SE:")
#print(df.loc[48, (slice(None)), :])
#df=setSubsistema(2)
#print("S:")
#print(df.loc[48, (slice(None)), :])
#df=setSubsistema(3)
#print("NE:")
#print(df.loc[48, (slice(None)), :])
#df=setSubsistema(4)
#print("N:")
#print(df.loc[48, (slice(None)), :])


##########------Filtro por faixa de serie------##########
subsistema = 1
variavel = 'ENA' #[CMO, ENA, EAR, Hid, Ter, Peq, Carga, Inter]
m = 'JUN'
valorMaxSE = 110
valorMinSE = 100
valorMaxMesesSE = 120
valorMinMesesSE =0

valorMaxS = 1000
valorMinS = 0
valorMaxMesesS = 1000
valorMinMesesS = 0

valorMaxNE = 150
valorMinNE = 0
valorMaxMesesNE = 1000
valorMinMesesNE =0

valorMaxN = 150
valorMinN = 0
valorMaxMesesN = 1000
valorMinMesesN =0

aux = ['JAN', 'FEV', 'MAR', 'ABR', 'MAI', 'JUN', 'JUL', 'AGO', 'SET', 'OUT', 'NOV', 'DEZ']
mesesPost =[]
mesesAnt = []
flag = 0
for i in range (0, len(aux)):
    if (aux[i]!= m) & flag:
        mesesPost.append(aux[i])
    elif (aux[i]!= m) & flag == 0:
        mesesAnt.append(aux[i])
    if aux[i] == m:
        flag =1

#Determinação do filtro:
#Para filtrar as séries considerando em outros subsistemas, são entrados na função de filtro um dataframe para comparação (definição do filtro) e outro para sua aplicação.
#No caso do filtro no qual a comparação é feita no próprio subsistema em questão (normalmente, o SE), entra-se os dois valores iguais
def filtro(dfComparacao, dfAplicacao, variavel, m, valorMax, valorMin, serieAnterior):
    seriesComparadas = dfComparacao.loc[(slice(None), m), variavel] #pd.Series com os valores das series a serem filtrados
    seriesFiltradas = dfAplicacao.loc[(slice(None), m), variavel]
    filtro = (seriesComparadas <= valorMax) & (seriesComparadas >= valorMin)
    resultFiltro = seriesFiltradas[filtro].index.get_level_values('serie') #LISTA com séries que atendem à condição do filtro
    #Montagem do dataframe:
    dfFilt = pd.DataFrame()
    auxSerie = []
    for s in resultFiltro:
        if s in serieAnterior:
            aux = dfAplicacao.loc[(s, slice(None)), : ]
            aux = pd.concat([aux])
            dfFilt = dfFilt.append(aux)
            auxSerie.append(s)
    propagadorSerie = pd.Series(auxSerie)
    #print("serie propagada: ", propagadorSerie, '\n')
    return(dfFilt, propagadorSerie)

#Aplicação recursiva dos filtros:
#Filtro aos outros subsistemas
subsistemas = []
print("Filtrando pelos outros subsistemas", '\n')
for i in range (1,5):
     if i != subsistema:
         subsistemas.append(i)
for s in subsistemas:
    print('Subsistema: ', s)
    if s == 2: #SUL
        df = setSubsistema(s)
        (dfFiltroSubsistema, serieAnterior) = filtro(df, setSubsistema(subsistema), variavel, m, valorMaxS, valorMinS, df.index.get_level_values('serie').drop_duplicates())
        print("Entra nos meses")
        for ms in mesesPost:
            (dfFiltroSubsistema, serieAnterior) = filtro(df,setSubsistema(subsistema), variavel, ms, valorMaxMesesS, valorMinMesesS, serieAnterior)
        print("Numero de seriesS: ", dfFiltroSubsistema.index.size / 13, '\n')
    elif s == 3: #NORDESTE
        df = setSubsistema(s)
        (dfFiltroSubsistema, serieAnterior)= filtro(df, setSubsistema(subsistema), variavel, m, valorMaxNE, valorMinNE, serieAnterior)
        for ms in mesesPost:
            (dfFiltroSubsistema, serieAnterior) = filtro(df,dfFiltroSubsistema, variavel, ms, valorMaxMesesNE, valorMinMesesNE, serieAnterior)
        print("Numero de seriesNE: ", dfFiltroSubsistema.index.size / 13, '\n')
    elif s == 4: #NORTE
        df = setSubsistema(s)
        (dfFiltroSubsistema, serieAnterior) = filtro(df, setSubsistema(subsistema), variavel, m, valorMaxN, valorMinN, serieAnterior)
        for ms in mesesPost:
            (dfFiltroSubsistema, serieAnterior) = filtro(df, setSubsistema(subsistema), variavel, ms, valorMaxMesesN, valorMinMesesN, serieAnterior)
        print("Numero de seriesN: ", dfFiltroSubsistema.index.size / 13, '\n')

#Filtro ao subsistema em questão
print("Filtrando por meses do subsistema ", str(subsistema), '\n')
df = setSubsistema(subsistema)
(dfFiltroMes, seriePropagada) = filtro(dfFiltroSubsistema, dfFiltroSubsistema, variavel, m, valorMaxSE, valorMinSE, serieAnterior)
print("filtromes: ", dfFiltroMes)
print("Numero de series: ", dfFiltroMes.index.size / 13, '\n')
# for ms in mesesPost:
#     print(ms)
#     (dfFiltroMes, seriePropagada) = filtro(dfFiltroMes, dfFiltroMes, variavel, ms, valorMaxMesesSE, valorMinMesesSE, seriePropagada)
print("Numero de series: ", dfFiltroMes.index.size/13, '\n')
#pd.Series(serieAnterior).to_excel(writer2) #debug
#writer2.save() #debug
#print("df Filtrado: ", '\n')
#print( dfFiltrado, '\n')

#Análise por produto
#Produto mensal:
produtoMensal = dfFiltroMes.reset_index(level = 'mes')
crit = produtoMensal.mes == 'JAN'
mensal = produtoMensal[crit]
for i in range (2, 14):
    crit = produtoMensal.mes == defineMes(i)
    mensal = pd.concat([mensal, produtoMensal[crit]], axis=0)
mensal = mensal.reset_index(level = 'serie', drop = True)
mensal = mensal.set_index(['mes'])
mensal = mensal.groupby(['mes'], sort = False).mean()

def produtos(dataFrame, mesInicio, mesFim): #sempre entrar com dataFrame = mensal
     produto = [0, 0, 0, 0, 0, 0, 0, 0]
     if mesInicio < 1 or mesFim > 12:
         print('Insira valores corretos para os meses')
     else:
         horas = [24*31, 24*28, 24*31, 24*30, 24*31, 24*30, 24*31, 24*31, 24*30, 24*31, 24*30, 24*31]
         horasTotais = 0
         somaCMO = 0
         somaHid = 0
         somaTer = 0
         somaPeq = 0
         somaCar = 0
         for i in range (mesInicio-1, mesFim):
             horasTotais = horasTotais + horas[i]
             somaCMO = somaCMO + horas[i]*dataFrame.iloc[i, 0]
             somaHid = somaHid + dataFrame.iloc[i, 3]
             somaTer = somaTer + dataFrame.iloc[i, 4]
             somaPeq = somaPeq + dataFrame.iloc[i, 5]
             somaCar = somaCar + dataFrame.iloc[i, 6]

         produto[0] = somaCMO/horasTotais
         produto[2] = dataFrame.iloc[mesFim - 1, 2]
         produto[3] = somaHid/(mesFim - mesInicio + 1)
         produto[4] = somaTer/(mesFim - mesInicio + 1)
         produto[5] = somaPeq/(mesFim - mesInicio + 1)
         produto[6] = somaCar/(mesFim - mesInicio + 1)
         return produto #[CMO_medio, 0, EAR(no fim do período do produto), Hid_med, Ter_mes, Peq_med, Carg_med, 0]

final = mensal
#produto 1sem: produtos(mensal, mes inicio do periodo = 1, mes fim do periodo = 6)
df1Sem = pd.DataFrame(produtos(mensal, 1, 6), columns= ['Prod:1sem'], index=['CMO', 'ENA', 'EAR', 'Hid', 'Ter', 'Peq', 'Carga', 'Inter'])
df1Sem = df1Sem.T
final = final.append(df1Sem)
#produto 2sem: produtos(mensal, mes inicio do periodo = 7, mes fim do periodo = 12)
df2Sem = pd.DataFrame(produtos(mensal, 7, 12), columns= ['Prod:2sem'], index=['CMO', 'ENA', 'EAR', 'Hid', 'Ter', 'Peq', 'Carga', 'Inter'])
df2Sem = df2Sem.T
final = final.append(df2Sem)
#produto 1tri: produtos(mensal, mes inicio do periodo = 1, mes fim do periodo = 3)
df1Tri = pd.DataFrame(produtos(mensal, 1, 3), columns= ['Prod:1tri'], index=['CMO', 'ENA', 'EAR', 'Hid', 'Ter', 'Peq', 'Carga', 'Inter'])
df1Tri = df1Tri.T
final = final.append(df1Tri)
#produto 2tri: produtos(mensal, mes inicio do periodo = 4, mes fim do periodo = 6)
df2Tri = pd.DataFrame(produtos(mensal, 4, 6), columns= ['Prod:2tri'],index=['CMO', 'ENA', 'EAR', 'Hid', 'Ter', 'Peq', 'Carga', 'Inter'])
df2Tri = df2Tri.T
final = final.append(df2Tri)
#produto 3tri: produtos(mensal, mes inicio do periodo = 7, mes fim do periodo = 8)
df3Tri = pd.DataFrame(produtos(mensal, 7, 8), columns= ['Prod:3tri'], index=['CMO', 'ENA', 'EAR', 'Hid', 'Ter', 'Peq', 'Carga', 'Inter'])
df3Tri = df3Tri.T
final = final.append(df3Tri)
#produto 4tri: produtos(mensal, mes inicio do periodo = 9, mes fim do periodo = 12)
df4Tri = pd.DataFrame(produtos(mensal, 9, 12), columns= ['Prod:4tri'], index=['CMO', 'ENA', 'EAR', 'Hid', 'Ter', 'Peq', 'Carga', 'Inter'])
df4Tri = df4Tri.T
final = final.append(df4Tri)

print(final)
final.to_excel(writer1,sheet_name= 'Molhado', index = True)
writer1.save()
writer1.close()

#Análise de balanço:
dfb = final
dfBalanco = pd.concat([dfb.pop('Hid'), dfb.pop('Ter'), dfb.pop('Peq'), dfb.pop('Inter')], axis = 1)
print(dfBalanco, '\n')
dfBalanco.to_excel(writer1, sheet_name= 'Balanço Molhado', index = True)
writer1.save()
writer1.close()