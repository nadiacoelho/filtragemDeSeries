import pandas as pd
import montaTabelaTotal

def is_equal(a, b):
    eps = 0.0000001
    return abs(a - b) < eps


dfSudeste = montaTabelaTotal.dfTotal1
dfSul = montaTabelaTotal.dfTotal2
dfNordeste = montaTabelaTotal.dfTotal3
dfNorte = montaTabelaTotal.dfTotal4