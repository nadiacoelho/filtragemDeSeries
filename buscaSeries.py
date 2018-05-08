import pandas as pd
import matplotlib.pyplot as plt
writer = pd.ExcelWriter('AnaliseNewave.xlsx', engine= 'openpyxl')
pd.set_option('display.width', 500)


#Os dataframes que serão usados no código inteiro. Se definidos como variável global do projeto, essas linhas podem ser suprimidas.
dfSudeste = pd.read_csv('Tabela1').set_index(['serie', 'mes'])
dfSul = pd.read_csv('Tabela2').set_index(['serie', 'mes'])
dfNordeste = pd.read_csv('Tabela3').set_index(['serie', 'mes'])
dfNorte = pd.read_csv('Tabela4').set_index(['serie', 'mes'])

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

##########------Filtro por faixa de serie------##########
subsistema = 1 # 1 (SE), 2 (S), 3 (NE), 4 (N)
variavel = 'Hid' #[CMO, ENA, EAR, Hid, Ter, Peq, Carga, Inter]
m = 'AGO'#['JAN', 'FEV', 'MAR', 'ABR', 'MAI', 'JUN', 'JUL', 'AGO', 'SET', 'OUT', 'NOV', 'DEZ']
valorMax = 20000
valorMin = 150

#Determinação do filtro:
df = setSubsistema(subsistema)
serie_a_filtrar = df.loc[(slice(None), m), variavel] #pd.Series com os valores das series a serem filtrados
filtro = (serie_a_filtrar <= valorMax) & (serie_a_filtrar >= valorMin)

resultFiltro = serie_a_filtrar[filtro].index.get_level_values('serie') #séries que atendem à condição

#Montagem do dataframe final:
dfFiltrado = pd.DataFrame()
for s in resultFiltro:
    aux = df.xs(s, level = 'serie')
    aux = pd.concat([aux], keys = [str(s)], names = ['serie'])
    dfFiltrado = dfFiltrado.append(aux)

#print(dfFiltrado, '\n')
print("Numero de series: ", dfFiltrado.index.size/13)

# #Exemplo do plot para o CMO
# numSeries = 3
# dfFiltrado.head(13*numSeries).plot(y= 'CMO', kind = 'bar')
# plt.show(block=True)

#Caso se deseje exportar para excel:
#dfFiltrado.to_excel(writer, sheet_name='Filtro por' + variavel, index = True)
#writer.save()

##########------Filtro por produto------##########
## Filtro por produto considerando as séries que atendem ao filtro por faixa de série. Para analisar todas as séries, modificar o dataframe de 'dfFiltrado' para 'df'

#Análise de balanço:
dfBalanco = pd.concat([dfFiltrado.pop('Hid'), dfFiltrado.pop('Ter'), dfFiltrado.pop('Peq'), dfFiltrado.pop('Inter'), dfFiltrado.pop('CMO')], axis = 1)
dfBalanco = dfBalanco.reset_index(level = 'mes')
#print(dfBalanco)

#Produto mensal:
mes = 'JUL'
crit = dfBalanco.mes == mes
mensal = dfBalanco[crit]
#print(mensal)

#Produto semestral:
#primeiro semestre
crit = (dfBalanco.mes == 'JAN') | (dfBalanco.mes == 'FEV') | (dfBalanco.mes == 'MAR') | (dfBalanco.mes == 'ABR') | (dfBalanco.mes == 'MAI') | (dfBalanco.mes == 'JUN')
primeiroSemestre = dfBalanco[crit]
#print(primeiroSemestre)

#segundo semestre
#def mediaSegSem(df):
#     if


crit = (dfBalanco.mes == 'JUL') | (dfBalanco.mes == 'AGO') | (dfBalanco.mes == 'SET') | (dfBalanco.mes == 'OUT') | (dfBalanco.mes == 'NOV') | (dfBalanco.mes == 'DEZ')
segundoSemestre = dfBalanco[crit]
#print(segundoSemestre.head(12))
segundoSemestre = segundoSemestre.groupby(['serie'], sort = False).mean()
#print(segundoSemestre.head(12))