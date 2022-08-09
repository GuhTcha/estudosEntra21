import pandas as pd

Url_or_file = "C:\Users\Gustavo\Downloads\PlanilhaDadosTeste - pessoas.csv"

def importa_planilha(colunas):

    df = pd.read.csv(Url_or_file, index_col=0, header=0, usecols=colunas)
    #dd = df.to_dict('index')
    #print(df)
    #print(dd)

    return df.to_dict('index')

#importa_planilha('id')