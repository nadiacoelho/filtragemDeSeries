import pandas as pd
pd.set_option('display.width', 400)
tabela = pd.read_fwf('eafbm002.out',delim_whitespace=1, skiprows= 2)

#o ano 2018(o ano vigente) no arquivo cmarg vai até a linha 6008 (2000 serie, 3 patamares por serie + estatisticas)
tabela2018 = tabela.iloc[:6002,:]

print(tabela2018)

#primeiras cinco series para teste:
#tabelaTeste = tabela.iloc[:17,:]
#print(tabelaTeste)