import pandas as pd

df=pd.read_excel('Controle Diário - JANEIRO.xlsx', sheet_name='RESUMO GERAL')

print(df.head(), '\n')

revenue= df['Unnamed: 7'][0] # "faturamento bruto" in Portuguese
revenue=float(revenue)
print(type(revenue))