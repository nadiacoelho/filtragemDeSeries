import pandas as pd
import montaTabelaTotal

def is_equal(a, b):
    eps = 0.0000001
    return abs(a - b) < eps


geracao = montaTabelaTotal.dfTotal1
variavel = 'CMO'

print(geracao[variavel])