import pandas as pd
pd.set_option('display.width', 400)

#importação do arquivo considerando o ano 2018(o ano vigente), que no arquivo vai até a linha 8000 (2000 series, 3 patamares + total para cada mês)
tabela1 = pd.read_fwf('gttot001.out',delim_whitespace=1, skiprows= 3)
tabela1_2018 = tabela1.iloc[:8001,:]
tabela2 = pd.read_fwf('gttot002.out',delim_whitespace=1, skiprows= 3)
tabela2_2018 = tabela2.iloc[:8001,:]
tabela3 = pd.read_fwf('gttot003.out',delim_whitespace=1, skiprows= 3)
tabela3_2018 = tabela3.iloc[:8001,:]
tabela4 = pd.read_fwf('gttot004.out',delim_whitespace=1, skiprows= 3)
tabela4_2018 = tabela4.iloc[:8001,:]

dfTer1 = pd.DataFrame(columns= ["JAN", "FEV", "MAR", "ABR", "MAI", "JUN", "JUL", "AGO", "SET", "OUT", "NOV", "DEZ", "MEDIA"])
dfTer2 = pd.DataFrame(columns= ["JAN", "FEV", "MAR", "ABR", "MAI", "JUN", "JUL", "AGO", "SET", "OUT", "NOV", "DEZ", "MEDIA"])
dfTer3 = pd.DataFrame(columns= ["JAN", "FEV", "MAR", "ABR", "MAI", "JUN", "JUL", "AGO", "SET", "OUT", "NOV", "DEZ", "MEDIA"])
dfTer4 = pd.DataFrame(columns= ["JAN", "FEV", "MAR", "ABR", "MAI", "JUN", "JUL", "AGO", "SET", "OUT", "NOV", "DEZ", "MEDIA"])

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
    listaAux = []
    i=4
    while i < len(tabela1_2018):
        valor = float(tabela1_2018.iloc[i, mes])
        i+=4
        listaAux.append(valor)
    label = defineMes(mes)
    dfTer1[label] = listaAux

    # 2 - SUL
    listaAux = []
    i=4
    while i < len(tabela2_2018):
        valor = float(tabela2_2018.iloc[i, mes])
        i+=4
        listaAux.append(valor)
    label = defineMes(mes)
    dfTer2[label] = listaAux

    #1 - NORDESTE
    listaAux = []
    i=4
    while i < len(tabela3_2018):
        valor = float(tabela3_2018.iloc[i, mes])
        i+=4
        listaAux.append(valor)
    label = defineMes(mes)
    dfTer3[label] = listaAux

    #4 - NORTE
    listaAux = []
    i=4
    while i < len(tabela4_2018):
        valor = float(tabela4_2018.iloc[i, mes])
        i+=4
        listaAux.append(valor)
    label = defineMes(mes)
    dfTer4[label] = listaAux
