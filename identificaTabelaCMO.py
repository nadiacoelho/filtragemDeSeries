import pandas as pd
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

def mediaPatamar(pesado, medio, leve):
    percentualPesado = 0.10
    percentualMedio = 0.52
    percentualLeve = 0.38
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
        precoMed = mediaPatamar(float(tabela1_2018.iloc[i, mes]),float(tabela1_2018.iloc[i+1, mes]),float(tabela1_2018.iloc[i+2, mes]))
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
        precoMed = mediaPatamar(float(tabela2_2018.iloc[i, mes]), float(tabela2_2018.iloc[i + 1, mes]), float(tabela2_2018.iloc[i + 2, mes]))
        i += 3
        if precoMed < piso:
            precoMed = piso
        if precoMed > teto:
            precoMed = teto
        precoMes.append(precoMed)
        precoMes.append(precoMed)
    label = defineMes(mes)
    dfCMO2[label] = precoMes

    #1 - NORDESTE
    precoMes = []
    i=2
    while i < len(tabela3_2018):
        precoMed = mediaPatamar(float(tabela3_2018.iloc[i, mes]),float(tabela3_2018.iloc[i+1, mes]),float(tabela3_2018.iloc[i+2, mes]))
        i+=3
        if precoMed < piso:
            precoMed = piso
        if precoMed > teto:
            precoMed = teto
        precoMes.append(precoMed)
        precoMes.append(precoMed)
    label = defineMes(mes)
    dfCMO3[label] = precoMes

    #4 - NORTE
    precoMes = []
    i=2
    while i < len(tabela4_2018):
        precoMed = mediaPatamar(float(tabela4_2018.iloc[i, mes]),float(tabela4_2018.iloc[i+1, mes]),float(tabela4_2018.iloc[i+2, mes]))
        i+=3
        if precoMed < piso:
            precoMed = piso
        if precoMed > teto:
            precoMed = teto
        precoMes.append(precoMed)
        precoMes.append(precoMed)
    label = defineMes(mes)
    dfCMO4[label] = precoMes
