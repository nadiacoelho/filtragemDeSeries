import pandas as pd
import matplotlib.pyplot as plt
writer = pd.ExcelWriter('AnaliseNewave.xlsx', engine= 'openpyxl')
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

##########------Filtro por faixa de serie------##########
subsistema = 1
variavel = 'Hid' #[CMO, ENA, EAR, Hid, Ter, Peq, Carga, Inter]
m = 'AGO'
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
print("Numero de series: ", dfFiltrado.index.size/13, '\n')

#Plot para o CMO
dfmensal = dfFiltrado.reset_index(level = 'serie').groupby(level='mes', sort = False).mean().round(decimals = 2, out = None)
#print(dfmensal, '\n')
ax = dfmensal.plot.bar(y = 'CMO')
for p in ax.patches:
    ax.annotate(str(p.get_height()), (p.get_x(), p.get_height()))
#plt.show(block=True)

#Análise de balanço:
#dfFilt = dfFiltrado
#dfBalanco = pd.concat([dfFilt.pop('Hid'), dfFilt.pop('Ter'), dfFilt.pop('Peq'), dfFilt.pop('Inter')], axis = 1)
#print(dfBalanco, '\n')
#balancoMensal = dfBalanco.reset_index(level = 'serie').groupby(level='mes', sort = False).mean().round(decimals = 2, out = None)
#print(dfmensal, '\n')
#ax = dfmensal.plot.bar(stacked = True, fontsize = 8)
#plt.show(block=True)

#Caso se deseje exportar para excel:
#dfFiltrado.to_excel(writer, sheet_name='Filtro por' + variavel, index = True)
#writer.save()

#Análise por produto
#Produto mensal:
produtoMensal = dfFiltrado.reset_index(level = 'mes')
crit = produtoMensal.mes == 'JAN'
mensal = produtoMensal[crit]

for i in range (2, 14):
    crit = produtoMensal.mes == defineMes(i)
    mensal = pd.concat([mensal, produtoMensal[crit]], axis=0)
mensal = mensal.reset_index(level = 'serie').set_index(['mes'])
mensal = mensal.groupby(['mes'], sort = False).mean()
print(mensal)

#Produto semestral:
#primeiro semestre:
horasPrimSem = pd.Series([744, 673, 744, 720, 744, 720], index=['JAN', 'FEV', 'MAR', 'ABR', 'MAI', 'JUN'])
primSem = mensal.drop(['JUL', 'AGO', 'SET', 'OUT', 'NOV', 'DEZ'])

#segundo semestre
horasSegSem = pd.Series([744, 744, 720, 744, 719, 744], index=['JUL', 'AGO', 'SET', 'OUT', 'NOV', 'DEZ'])
segSem = mensal.drop(['JAN', 'FEV', 'MAR', 'ABR', 'MAI', 'JUN'])
