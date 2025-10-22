import pandas as pd

month=input('Enter the month: ')

df_expenses=pd.read_excel('CONTROLE DIÁRIO - teste.xlsx', sheet_name='RESUMO DESPESAS')
df_expenses['MES']=month

with pd.ExcelWriter('CONTROLE DIÁRIO - teste.xlsx',         # File Handle to write on the file.
                    engine='openpyxl',
                    mode='a',                               # 'a' append: add things to the file.
                    if_sheet_exists='replace'               # Substitutes the sheet if already exists.
                    ) as writer:
        df_expenses.to_excel(writer, sheet_name='RESUMO DESPESAS', index=False)
#print(df_expenses.head(), '\n')
#print(df_expenses.dtypes, '\n')
#print(df_expenses.shape)

print('Done!')

#df_revenue=pd.read_excel('CONTROLE DIÁRIO - teste.xlsx', sheet_name='RESUMO RECEITAS')

#print(df_revenue.head(), '\n')
#print(df_revenue.dtypes, '\n')
#print(df_revenue.shape)