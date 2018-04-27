import pandas as pd
pd.set_option('display.width', 400)
tabela = pd.read_fwf('cmarg002.out',delim_whitespace=1, skiprows= 2)

#o ano 2018(o ano vigente) no arquivo cmarg vai até a linha 6008 (2000 serie, 3 patamares por serie + estatisticas)
tabela2018 = tabela.iloc[:6008,:]

tabela2018.iloc[6002,0] = "MEDIA"
tabela2018.iloc[6003,0] = "DESVIO PADRAO"
tabela2018.iloc[6004,0] = "MIN"
tabela2018.iloc[6005,0] = "P5"
tabela2018.iloc[6006,0] = "P95"
tabela2018.iloc[6007,0] = "MAX"

print(tabela2018)

#primeiras cinco series para teste:
#tabelaTeste = tabela.iloc[:17,:]
#print(tabelaTeste)