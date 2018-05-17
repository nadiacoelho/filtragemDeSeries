import pandas as pd
pd.set_option('display.width', 400)

#monta o dataframe com multiindex:
arrays = pd.MultiIndex.from_product([['1', '2', '3', '4'], ['pequenas', 'carga']], names = ['subsistema', 'variavel'])
index = ['JAN', 'FEV', 'MAR', 'ABR', 'MAI', 'JUN', 'JUL', 'AGO', 'SET', 'OUT', 'NOV', 'DEZ']
dfSistema = pd.DataFrame(index= index,columns=arrays)

# #Lê pequenas:
pequenas = pd.read_fwf('SISTEMA.DAT',delim_whitespace=1, skiprows= 124, nrows= 19)
pequenas = pequenas.transpose()
pequenas.insert(loc = 0, column = 'index', value = ['ANO','JAN', 'FEV', 'MAR', 'ABR', 'MAI', 'JUN', 'JUL', 'AGO', 'SET', 'OUT', 'NOV', 'DEZ'])
pequenas = pequenas.set_index('index')

pequenas1=pequenas.pop(0)
pequenas1 = pequenas1.rename("peqSudeste")
pequenas1.pop("ANO")
dfSistema.loc[:, ('1','pequenas')] = pequenas1

pequenas2=pequenas.pop(6)
pequenas2 = pequenas2.rename("peqSul")
pequenas2.pop("ANO")
dfSistema.loc[:, ('2','pequenas')] = pequenas2
pequenas3=pequenas.pop(12)
pequenas3 = pequenas3.rename("peqNordeste")
pequenas3.pop("ANO")
dfSistema.loc[:, ('3','pequenas')] = pequenas3
pequenas4=pequenas.pop(18)
pequenas4 = pequenas4.rename("peqNorte")
pequenas4.pop("ANO")
dfSistema.loc[:, ('4','pequenas')] = pequenas4

#Lê cargas:
#porque a leitura da tabela de cargas não é formatada (como a de geração não despachada), tive que adotar a solução:
#limpei a tabela para conter apenas os dados relativos a 2018 (ano vigente)
#coletei linha a linha, e adicionei ao dataframe de trás para frente, de forma que os meses que não tem geração não são preenchidos no dataframe.
#podemos, depois, reajustar esses valores para 0

cargas = pd.read_fwf('SISTEMA.DAT',delim_whitespace=1, skiprows= 92, nrows= 22)
cargas = cargas.drop([1,2,3,4,5,6,8,9,10,11,12,13,15,16,17,18,19,20])
def defineMes(mes):
    if mes == 1:
        return "JAN"
    if mes == 2:
        return "FEV"
    if mes == 3:
        return "MAR"
    if mes == 4:
        return "ABR"
    if mes == 5:
        return "MAI"
    if mes == 6:
        return "JUN"
    if mes == 7:
        return "JUL"
    if mes == 8:
        return "AGO"
    if mes == 9:
        return "SET"
    if mes == 10:
        return "OUT"
    if mes == 11:
        return "NOV"
    if mes == 12:
        return "DEZ"

cargas1= cargas.iloc[0,:]
cargas1 = cargas1.rename("cargaSudeste")
ultimo = cargas1.size - 1
mes = 12 #comeca em DEZ
while ultimo >=2 :
    dfSistema.loc[defineMes(mes), ('1', 'carga')] = float(cargas1.iloc[ultimo])
    mes-=1
    ultimo-=1

cargas2= cargas.iloc[1,:]
cargas2 = cargas2.rename("cargaSul")
ultimo = cargas2.size - 1
mes = 12 #comeca em DEZ
while ultimo >=2 :
    dfSistema.loc[defineMes(mes), ('2', 'carga')] = float(cargas2.iloc[ultimo])
    mes-=1
    ultimo-=1

cargas3= cargas.iloc[2,:]
cargas3 = cargas3.rename("cargaNordeste")
ultimo = cargas1.size - 1
mes = 12 #comeca em DEZ
while ultimo >=2 :
    dfSistema.loc[defineMes(mes), ('3', 'carga')] = float(cargas3.iloc[ultimo])
    mes-=1
    ultimo-=1

cargas4= cargas.iloc[3,:]
cargas4 = cargas4.rename("cargaNorte")
ultimo = cargas1.size - 1
mes = 12 #comeca em DEZ
while ultimo >=2 :
    dfSistema.loc[defineMes(mes), ('4', 'carga')] = float(cargas4.iloc[ultimo])
    mes-=1
    ultimo-=1

while mes > 0:
    dfSistema.loc[defineMes(mes), ('1', 'pequenas')] = 0
    dfSistema.loc[defineMes(mes), ('2', 'pequenas')] = 0
    dfSistema.loc[defineMes(mes), ('3', 'pequenas')] = 0
    dfSistema.loc[defineMes(mes), ('4', 'pequenas')] = 0
    mes-=1

dfSistema = dfSistema.fillna(0)
print(dfSistema)