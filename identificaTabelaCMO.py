import pandas as pd
import identificaTabelaEAR
pd.set_option('display.width', 400)

#LIMITES DE PREÇO:
piso = 40.16
teto = 505.18

tabela1 = pd.read_fwf('cmarg001.out',delim_whitespace=1, skiprows= 2)
tabela1_2018 = tabela1.iloc[:6002,:]
tabela2 = pd.read_fwf('cmarg002.out',delim_whitespace=1, skiprows= 2)
tabela2_2018 = tabela2.iloc[:6002,:]
tabela3 = pd.read_fwf('cmarg003.out',delim_whitespace=1, skiprows= 2)
tabela3_2018 = tabela3.iloc[:6002,:]
tabela4 = pd.read_fwf('cmarg004.out',delim_whitespace=1, skiprows= 2)
tabela4_2018 = tabela4.iloc[:6002,:]

dfCMO1 = pd.DataFrame(columns= ["JAN", "FEV", "MAR", "ABR", "MAI", "JUN", "JUL", "AGO", "SET", "OUT", "NOV", "DEZ", "MEDIA"])
dfCMO2 = pd.DataFrame(columns= ["JAN", "FEV", "MAR", "ABR", "MAI", "JUN", "JUL", "AGO", "SET", "OUT", "NOV", "DEZ", "MEDIA"])
dfCMO3 = pd.DataFrame(columns= ["JAN", "FEV", "MAR", "ABR", "MAI", "JUN", "JUL", "AGO", "SET", "OUT", "NOV", "DEZ", "MEDIA"])
dfCMO4 = pd.DataFrame(columns= ["JAN", "FEV", "MAR", "ABR", "MAI", "JUN", "JUL", "AGO", "SET", "OUT", "NOV", "DEZ", "MEDIA"])

def mediaPatamar(pesado, medio, leve, mes):
    if mes == 1:
        percentualPesado = 0.1048
        percentualMedio = 0.5229
        percentualLeve = 0.3723
    if mes == 2:
        percentualPesado = 0.1025
        percentualMedio = 0.5171
        percentualLeve = 0.3804
    if mes == 3:
        percentualPesado = 0.1048
        percentualMedio = 0.5229
        percentualLeve = 0.3723
    if mes == 4:
        percentualPesado = 0.1000
        percentualMedio = 0.5083
        percentualLeve = 0.3917
    if mes == 5:
        percentualPesado = 0.1008
        percentualMedio = 0.5108
        percentualLeve = 0.3583
    if mes == 6:
        percentualPesado = 0.1083
        percentualMedio = 0.5334
        percentualLeve = 0.3583
    if mes == 7:
        percentualPesado = 0.1048
        percentualMedio = 0.5229
        percentualLeve = 0.3723
    if mes == 8:
        percentualPesado = 0.1089
        percentualMedio = 0.5349
        percentualLeve = 0.3562
    if mes == 9:
        percentualPesado = 0.1000
        percentualMedio = 0.5083
        percentualLeve = 0.3917
    if mes == 10:
        percentualPesado = 0.1048
        percentualMedio = 0.5229
        percentualLeve = 0.3723
    if mes == 11:
        percentualPesado = 0.1001
        percentualMedio = 0.5091
        percentualLeve = 0.3908
    if mes == 12:
        percentualPesado = 0.1008
        percentualMedio = 0.5108
        percentualLeve = 0.3884
    if mes == 13:
        percentualPesado = 0.1034
        percentualMedio = 0.5187
        percentualLeve = 0.3779
    #percentualPesado = 0.1034
    #percentualMedio = 0.5187
    #percentualLeve = 0.3779
    media = (pesado*percentualPesado) + (medio*percentualMedio) + (leve*percentualLeve)
    return (media)
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
    if mes == 13:
        return "MEDIA"
for mes in range (1,14):
    #1 - SUDESTE
    precoMes = []
    i=2
    while i < len(tabela1_2018):
        precoMed = mediaPatamar(float(tabela1_2018.iloc[i, mes]),float(tabela1_2018.iloc[i+1, mes]),float(tabela1_2018.iloc[i+2, mes]), mes)
        i+=3
        if precoMed < piso:
            precoMed = piso
        if precoMed > teto:
            precoMed = teto
        precoMes.append(precoMed)
    label = defineMes(mes)
    dfCMO1[label] = precoMes

    # 2 - SUL
    precoMes = []
    i = 2
    while i < len(tabela2_2018):
        precoMed = mediaPatamar(float(tabela2_2018.iloc[i, mes]), float(tabela2_2018.iloc[i + 1, mes]), float(tabela2_2018.iloc[i + 2, mes]), mes)
        i += 3
        if precoMed < piso:
            precoMed = piso
        if precoMed > teto:
            precoMed = teto
        precoMes.append(precoMed)
    label = defineMes(mes)
    dfCMO2[label] = precoMes

    #1 - NORDESTE
    precoMes = []
    i=2
    while i < len(tabela3_2018):
        precoMed = mediaPatamar(float(tabela3_2018.iloc[i, mes]),float(tabela3_2018.iloc[i+1, mes]),float(tabela3_2018.iloc[i+2, mes]), mes)
        i+=3
        if precoMed < piso:
            precoMed = piso
        if precoMed > teto:
            precoMed = teto
        precoMes.append(precoMed)
    label = defineMes(mes)
    dfCMO3[label] = precoMes

    #4 - NORTE
    precoMes = []
    i=2
    while i < len(tabela4_2018):
        precoMed = mediaPatamar(float(tabela4_2018.iloc[i, mes]),float(tabela4_2018.iloc[i+1, mes]),float(tabela4_2018.iloc[i+2, mes]), mes)
        i+=3
        if precoMed < piso:
            precoMed = piso
        if precoMed > teto:
            precoMed = teto
        precoMes.append(precoMed)
    label = defineMes(mes)
    dfCMO4[label] = precoMes


print(dfCMO1)

writer1 = pd.ExcelWriter("Debug.xlsx", engine= 'openpyxl')
dfCMO1.to_excel(writer1)
writer1.save()