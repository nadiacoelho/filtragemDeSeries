import pandas as pd
pd.set_option('display.width', 400)

tabela = pd.read_fwf('cmarg002.out',delim_whitespace=1, skiprows= 2)
#o ano 2018 no arquivo cmarg vai até a linha 6009 (2000 serie, 3 patamares por serie
print(tabela.head(6020))
print(tabela.iloc[4,0])
print(tabela.iloc[4,1])
print(tabela.iloc[4,2])
print(tabela.iloc[4,3])
print(tabela.iloc[4,4])
print(tabela.iloc[4,5])
print(tabela.iloc[4,6])
print(tabela.iloc[4,5]+tabela.iloc[4,6])
#ano2018 = tabela.iloc[:6009,:]
#print(ano2018)

def mediaPatamar(pesado, medio, leve):
    percentualPesado = 0,10
    percentualMedio = 0,52
    percentualLeve = 0,38

    media = pesado*percentualPesado + medio*percentualMedio + leve*percentualLeve
    return (media)