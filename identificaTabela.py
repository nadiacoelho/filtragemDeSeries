import pandas as pd
pd.set_option('display.width', 400)

tabela = pd.read_fwf('cmarg002.out',delim_whitespace=1, skiprows= 2)
#o ano 2018 no arquivo cmarg vai até a linha 6009 (2000 serie, 3 patamares por serie
print(tabela.head(5))


def mediaPatamar(pesado, medio, leve):
    percentualPesado = 0.10
    percentualMedio = 0.52
    percentualLeve = 0.38

    media = pesado*percentualPesado + medio*percentualMedio + leve*percentualLeve
    return (media)

precoMes=[]
for mes in range (1,14):
    for i in range (2, 15):
        print(precoMes)
        print('i ',i)
        print('mes ', mes)
        print(tabela.iloc[i,mes])
        precoMes[mes-1] = mediaPatamar(tabela.iloc[i, mes],tabela.iloc[i+1, mes],tabela.iloc[i+2, mes])
        i+=3
    mes+=1

print(precoMes)